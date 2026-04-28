const API = 'http://144.91.118.72:8080/api/v1/news/';

// ─── GET: Barcha yangiliklar ───────────────────────────────────────────────
async function getNews() {
  const list = document.getElementById('news-list');
  list.innerHTML = '<p class="hint">Yuklanmoqda...</p>';

  const response = await fetch(API);
  const data = await response.json();

  if (data.results.length === 0) {
    list.innerHTML = '<p class="hint">Yangiliklar yo\'q</p>';
    return;
  }

  list.innerHTML = '';
  data.results.forEach(item => {
    list.innerHTML += `
      <div class="news-item">
        <h3>
          ${item.title}
          <span class="badge ${item.is_published ? 'yes' : 'no'}">
            ${item.is_published ? 'Chop etilgan' : 'Chop etilmagan'}
          </span>
        </h3>
        <div class="meta">ID: ${item.id} | Muallif: ${item.author || '—'} | ${item.created_at.slice(0, 10)}</div>
        <p>${item.description}</p>
        <div class="actions">
          <button class="btn yellow" onclick="editNews(${item.id})">Tahrirlash (PUT)</button>
          <button class="btn red"    onclick="deleteNews(${item.id})">O'chirish (DELETE)</button>
        </div>
      </div>
    `;
  });
}

// ─── POST yoki PUT: Saqlash ────────────────────────────────────────────────
async function saveNews() {
  const id    = document.getElementById('edit-id').value;
  const title = document.getElementById('input-title').value.trim();
  const desc  = document.getElementById('input-description').value.trim();
  const author= document.getElementById('input-author').value.trim();
  const pub   = document.getElementById('input-published').checked;

  if (!title || !desc) {
    showMsg('Sarlavha va matnni to\'ldiring!', 'error');
    return;
  }

  const body = { title, description: desc, author, is_published: pub };

  // id bo'lsa → PUT (tahrirlash), bo'lmasa → POST (yaratish)
  const url    = id ? `${API}${id}/` : API;
  const method = id ? 'PUT' : 'POST';

  const response = await fetch(url, {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });

  if (response.ok) {
    showMsg(id ? 'Yangilik tahrirlandi!' : 'Yangilik qo\'shildi!', 'success');
    resetForm();
    getNews();
  } else {
    showMsg('Xatolik yuz berdi!', 'error');
  }
}

// ─── GET <id>: Tahrirlash uchun ma'lumot olish ─────────────────────────────
async function editNews(id) {
  const response = await fetch(`${API}${id}/`);
  const item = await response.json();

  document.getElementById('edit-id').value          = item.id;
  document.getElementById('input-title').value       = item.title;
  document.getElementById('input-description').value = item.description;
  document.getElementById('input-author').value      = item.author || '';
  document.getElementById('input-published').checked = item.is_published;
  document.getElementById('form-title').textContent  = `Tahrirlash (PUT) — ID: ${item.id}`;

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ─── DELETE: O'chirish ─────────────────────────────────────────────────────
async function deleteNews(id) {
  if (!confirm(`ID ${id} ni o'chirasizmi?`)) return;

  const response = await fetch(`${API}${id}/`, { method: 'DELETE' });

  if (response.status === 204) {
    showMsg('Yangilik o\'chirildi!', 'success');
    getNews();
  } else {
    showMsg('O\'chirishda xatolik!', 'error');
  }
}

// ─── Formani tozalash ──────────────────────────────────────────────────────
function resetForm() {
  document.getElementById('edit-id').value           = '';
  document.getElementById('input-title').value        = '';
  document.getElementById('input-description').value  = '';
  document.getElementById('input-author').value       = '';
  document.getElementById('input-published').checked  = true;
  document.getElementById('form-title').textContent   = 'Yangilik qo\'shish (POST)';
}

// ─── Xabar ko'rsatish ──────────────────────────────────────────────────────
function showMsg(text, type) {
  const old = document.querySelector('.msg');
  if (old) old.remove();

  const div = document.createElement('div');
  div.className = `msg ${type}`;
  div.textContent = text;
  document.querySelector('.container').prepend(div);

  setTimeout(() => div.remove(), 3000);
}

// Sahifa ochilganda ro'yxatni yukla
getNews();
