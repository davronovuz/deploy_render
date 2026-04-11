// 1. Yangi 'li' elementi yaratamiz
const newItem = document.createElement('li');

// 2. Ichiga matn yozamiz
newItem.textContent = 'Yangi vazifa qo\'shildi';

// 3. Sahifadagi mavjud 'ul' elementini topamiz va unga qo'shamiz
const list = document.querySelector('#task-list');
list.appendChild(newItem);



// READ
// ID orqali tanlash
const title = document.querySelector('#main-title');
console.log(title.textContent); // Element matnini konsolga chiqaradi

// Barcha 'li' elementlarini olish
const allItems = document.querySelectorAll('li');
allItems.forEach(item => console.log(item.innerText));



// UDPATE
const firstItem = document.querySelector('li:first-child');

// Matnni o'zgartirish
firstItem.textContent = 'Yangilangan vazifa nomi';

// CSS uslubini o'zgartirish
firstItem.style.color = 'blue';
firstItem.style.fontWeight = 'bold';

// Atributni o'zgartirish (masalan, class qo'shish)
firstItem.classList.add('completed');


const itemToDelete = document.querySelector('.old-task');

// Elementni o'chirish
if (itemToDelete) {
    itemToDelete.remove();
}

// Alternativ: Ota element orqali bolani o'chirish
// list.removeChild(itemToDelete);


<ul id="myList"></ul>

const list = document.getElementById('myList');

// --- CREATE ---
function addTask(text) {
    const li = document.createElement('li');
    li.innerHTML = `
        <span>${text}</span>
        <button class="edit-btn">Tahrirlash</button>
        <button class="delete-btn">O'chirish</button>
    `;
    list.appendChild(li);

    // --- DELETE (tugmaga biriktirish) ---
    li.querySelector('.delete-btn').onclick = () => li.remove();

    // --- UPDATE ---
    li.querySelector('.edit-btn').onclick = () => {
        const newText = prompt("Yangi matnni kiriting:", li.querySelector('span').textContent);
        if (newText) {
            li.querySelector('span').textContent = newText;
        }
    };
}

// Sinov uchun:
addTask("Dars qilish");
addTask("Kitob o'qish");