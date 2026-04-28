const API = 'http://144.91.118.72:8080/api/v1/news/';


// ════════════════════════════════════════════════════════════════
// GET — yangiliklarni olish
// ════════════════════════════════════════════════════════════════
async function olish() {
  const res  = await fetch(API);
  const data = await res.json();

  document.getElementById('grid').innerHTML = data.results.map(item => `
    <div class="card">
      <img src="${item.image || 'https://placehold.co/400x180?text=Rasm'}" />
      <div class="card-body">
        <h3>${item.title}</h3>
        <p>${item.description}</p>
        <button class="edit"   onclick="tahrirlash(${item.id})">Tahrirlash</button>
        <button class="delete" onclick="ochirish(${item.id})">O'chirish</button>
      </div>
    </div>
  `).join('');
}


// ════════════════════════════════════════════════════════════════
// POST — yangi yangilik qo'shish
// ════════════════════════════════════════════════════════════════
async function qoshish(title, description, author) {
  const res = await fetch(API, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, description, author })
  });
  return res;
}


// ════════════════════════════════════════════════════════════════
// PUT — yangilikni yangilash
// ════════════════════════════════════════════════════════════════
async function yangilash(id, title, description, author) {
  const res = await fetch(API + id + '/', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, description, author })
  });
  return res;
}


// ════════════════════════════════════════════════════════════════
// DELETE — yangilikni o'chirish
// ════════════════════════════════════════════════════════════════
async function ochirish(id) {
  await fetch(API + id + '/', { method: 'DELETE' });
  olish();
}


// ════════════════════════════════════════════════════════════════
// Tugma bosilganda — saqlash (POST yoki PUT chaqiradi)
// ════════════════════════════════════════════════════════════════
async function saqlash() {
  const id          = document.getElementById('id').value;
  const title       = document.getElementById('title').value;
  const description = document.getElementById('description').value;
  const author      = document.getElementById('author').value;
  const xabar       = document.getElementById('xabar');

  let res;
  if (id) {
    res = await yangilash(id, title, description, author);
  } else {
    res = await qoshish(title, description, author);
  }

  if (res.ok) {
    xabar.style.color = 'green';
    xabar.textContent = id ? 'Yangilandi!' : 'Qoshildi!';
    document.getElementById('id').value          = '';
    document.getElementById('title').value       = '';
    document.getElementById('description').value = '';
    document.getElementById('author').value      = '';
    olish();
  } else {
    const xato = await res.json();
    xabar.style.color = 'red';
    xabar.textContent = 'Xato: ' + JSON.stringify(xato);
  }
}


// ════════════════════════════════════════════════════════════════
// Tahrirlash tugmasi — formani to'ldiradi
// ════════════════════════════════════════════════════════════════
async function tahrirlash(id) {
  const res  = await fetch(API + id + '/');
  const item = await res.json();

  document.getElementById('id').value          = item.id;
  document.getElementById('title').value       = item.title;
  document.getElementById('description').value = item.description;
  document.getElementById('author').value      = item.author;
}


// Sahifa ochilganda yangiliklarni yuklash
olish();
