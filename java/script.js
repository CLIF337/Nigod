// ==================== ГАРМОШКА ====================
var acc = document.getElementsByClassName("accordion");
for (var i = 0; i < acc.length; i++) {
    acc[i].onclick = function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    };
}

// ==================== ЗАДАЧА 1: ДАТА И ВРЕМЯ ====================
function showTime() {
    var d = new Date();
    var days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
    var dayOfWeek = days[d.getDay()];

    var day = d.getDate();
    var month = d.getMonth() + 1;
    var year = d.getFullYear();

    var hours = d.getHours();
    var minutes = d.getMinutes();
    var seconds = d.getSeconds();
    
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12;

    if (day < 10) day = "0" + day;
    if (month < 10) month = "0" + month;
    if (hours < 10) hours = "0" + hours;
    if (minutes < 10) minutes = "0" + minutes;
    if (seconds < 10) seconds = "0" + seconds;

    var firstLine = year + "-" + day + "-" + month + ", " + dayOfWeek;
    var secondLine = hours + ":" + minutes + ":" + seconds + " " + ampm;

    document.getElementById("clock").innerHTML = firstLine + "<br>" + secondLine;
}
setInterval(showTime, 1000);
showTime();

// ==================== ЗАДАЧА 2: КАЛЕНДАРЬ ====================
let currentDate = new Date();
let selectedDate = null;

const months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
];
const daysOfWeek = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"];

function renderCalendar() {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    
    const monthYearDisplay = document.getElementById("current-month-year");
    if (monthYearDisplay) {
        monthYearDisplay.textContent = `${months[month]} ${year}`;
    }
    
    const calendarContainer = document.getElementById("calendar-container");
    if (!calendarContainer) return;
    
    calendarContainer.innerHTML = "";
    const table = document.createElement("table");
    table.className = "calendar-table";
    
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");
    daysOfWeek.forEach(day => {
        const th = document.createElement("th");
        th.textContent = day;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);
    
    const tbody = document.createElement("tbody");
    const firstDay = new Date(year, month, 1);
    const startDayOfWeek = firstDay.getDay();
    let startOffset = startDayOfWeek === 0 ? 6 : startDayOfWeek - 1;
    
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    let dayCounter = 1;
    let row = document.createElement("tr");
    
    for (let i = 0; i < startOffset; i++) {
        const td = document.createElement("td");
        td.textContent = "";
        td.className = "empty-cell";
        row.appendChild(td);
    }
    
    for (let day = 1; day <= daysInMonth; day++) {
        const td = document.createElement("td");
        td.textContent = day;
        
        const currentDay = new Date(year, month, day);
        const dayOfWeekNum = currentDay.getDay();
        if (dayOfWeekNum === 0 || dayOfWeekNum === 6) {
            td.classList.add("weekend");
        }
        
        const today = new Date();
        if (today.getFullYear() === year && today.getMonth() === month && today.getDate() === day) {
            td.classList.add("today");
        }
        
        if (selectedDate && selectedDate.getFullYear() === year && selectedDate.getMonth() === month && selectedDate.getDate() === day) {
            td.classList.add("selected");
        }
        
        td.addEventListener("click", (function(y, m, d) {
            return function() { selectDate(y, m, d); };
        })(year, month, day));
        
        row.appendChild(td);
        
        if ((dayOfWeekNum === 0 && day !== daysInMonth) || day === daysInMonth) {
            while (row.children.length < 7) {
                const td = document.createElement("td");
                td.textContent = "";
                td.className = "empty-cell";
                row.appendChild(td);
            }
            tbody.appendChild(row);
            row = document.createElement("tr");
        }
    }
    
    table.appendChild(tbody);
    calendarContainer.appendChild(table);
}

function selectDate(year, month, day) {
    selectedDate = new Date(year, month, day);
    const selectedDateDisplay = document.getElementById("selected-date");
    if (selectedDateDisplay) {
        selectedDateDisplay.textContent = `Выбранная дата: ${day} ${months[month]} ${year} года`;
        selectedDateDisplay.style.opacity = "0";
        setTimeout(() => { selectedDateDisplay.style.opacity = "1"; }, 100);
    }
    renderCalendar();
}

function prevMonth() { currentDate.setMonth(currentDate.getMonth() - 1); renderCalendar(); }
function nextMonth() { currentDate.setMonth(currentDate.getMonth() + 1); renderCalendar(); }
function goToToday() { currentDate = new Date(); renderCalendar(); }

document.addEventListener("DOMContentLoaded", function() {
    renderCalendar();
});

// ==================== ЗАДАЧА 3: DOM-ДЕРЕВО (ТОЛЬКО СПИСКИ) ====================
document.addEventListener("DOMContentLoaded", function() {
    const countBtn = document.getElementById("count-btn");
    if (countBtn) {
        countBtn.addEventListener("click", function() {
            const ulLists = document.getElementsByTagName("ul");
            const olLists = document.getElementsByTagName("ol");
            const totalLists = ulLists.length + olLists.length;
            const allLists = [...ulLists, ...olLists];
            const result = document.getElementById("dom-result");
            if (result) {
                result.innerHTML = `
                    <strong>Найдено списков: ${totalLists}</strong><br>
                    - Маркированных списков (&lt;ul&gt;): ${ulLists.length}<br>
                    - Нумерованных списков (&lt;ol&gt;): ${olLists.length}
                `;
                highlightLists(allLists);
            }
        });
    }
});

function highlightLists(lists) {
    document.querySelectorAll('.highlight-list').forEach(list => list.classList.remove('highlight-list'));
    lists.forEach(list => {
        list.classList.add('highlight-list');
        setTimeout(() => list.classList.remove('highlight-list'), 2000);
    });
}

// ==================== ЗАДАЧА 4: ТЕКСТ В 5 БЛОКАХ (30 мс, ПОСЛЕДОВАТЕЛЬНО) ====================
// ==================== ЗАДАЧА 4: ТЕКСТ В 5 БЛОКАХ (500 мс, ПОСЛЕДОВАТЕЛЬНО) ====================
(function() {
    const blocks = document.querySelectorAll('#task4-blocks .task4-block');
    let task4Interval = null;
    let currentBlockIdx = 0;

    function clearAllTexts() {
        blocks.forEach((block, i) => {
            block.textContent = `Блок ${i+1}`;
            block.classList.remove('active-text');
        });
    }

    function showTextInBlock(index) {
        clearAllTexts(); // очищаем все блоки
        if (blocks[index]) {
            blocks[index].textContent = `✨ Текст ${index+1} ✨\n${new Date().toLocaleTimeString()}`;
            blocks[index].classList.add('active-text');
        }
    }

    function startTask4() {
        if (task4Interval) clearInterval(task4Interval);
        task4Interval = setInterval(() => {
            showTextInBlock(currentBlockIdx);
            currentBlockIdx = (currentBlockIdx + 1) % blocks.length;
        }, 30); // ← изменено с 30 на 500 мс
    }

    function stopTask4() {
        if (task4Interval) {
            clearInterval(task4Interval);
            task4Interval = null;
        }
        clearAllTexts();
    }

    const startBtn = document.getElementById('task4-start-btn');
    const stopBtn = document.getElementById('task4-stop-btn');
    if (startBtn && stopBtn) {
        startBtn.addEventListener('click', startTask4);
        stopBtn.addEventListener('click', stopTask4);
        startTask4();
    }
})();

// ==================== ЗАДАЧА 5: ССЫЛКИ В DIV, УДАЛЕНИЕ СВЕРХУ ====================
(function() {
    const container = document.getElementById('dynamic-links');
    if (!container) return;

    function addLink() {
        let linkText = prompt('Введите текст ссылки:', 'Пример ссылки');
        if (linkText === null) return;
        
        const wrapper = document.createElement('div');
        wrapper.className = 'link-wrapper';
        
        const link = document.createElement('a');
        link.href = '#';
        link.textContent = linkText;
        link.style.color = '#1e88e5';
        link.style.textDecoration = 'none';
        link.onclick = (e) => {
            e.preventDefault();
            alert(`Переход по ссылке: ${linkText}`);
        };
        
        wrapper.appendChild(link);
        container.appendChild(wrapper);
    }

    function removeTopLink() {
        const firstItem = container.firstElementChild;
        if (!firstItem) {
            alert('Нет элементов для удаления');
            return;
        }
        const link = firstItem.querySelector('a');
        const content = link ? link.textContent : 'неизвестный элемент';
        if (confirm(`Удалить элемент: "${content}"?`)) {
            alert(`Удалено содержимое: ${content}`);
            firstItem.remove();
        }
    }

    document.getElementById('add-link-btn')?.addEventListener('click', addLink);
    document.getElementById('remove-top-btn')?.addEventListener('click', removeTopLink);
})();

// ==================== ЗАДАЧА 6: Выход мыши с картинки → слова РАЗ, ДВА, ТРИ, ЧЕТЫРЕ, ПЯТЬ ====================
(function() {
    const cells = document.querySelectorAll('.task6-cell');
    const displayDiv = document.getElementById('task6-display');

    function copyCellText(event) {
        const cell = event.currentTarget;
        const text = cell.textContent;
        if (displayDiv) {
            displayDiv.textContent = text;
        }
    }

    cells.forEach(cell => {
        cell.addEventListener('mouseleave', copyCellText);
    });

    // Начальное сообщение
    if (displayDiv && displayDiv.textContent === 'Выйдите мышью с любой ячейки') {
        // оставляем как есть
    }
})();