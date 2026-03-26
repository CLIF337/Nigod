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

// =====================================
// ЗАДАЧА 1: Дата и время
// =====================================
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
    
    // Определяем AM или PM
    var ampm = hours >= 12 ? 'PM' : 'AM';
    
    // Конвертируем часы в 12-часовой формат
    hours = hours % 12;
    hours = hours ? hours : 12; // 0 часов становится 12

    // Добавляем ведущие нули
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

// =====================================
// ЗАДАЧА 2: Календарь
// =====================================
// ========== ЗАДАЧА 2: КАЛЕНДАРЬ (С ПЕРЕКЛЮЧЕНИЕМ МЕСЯЦЕВ) ==========

let currentDate = new Date(); // Текущая отображаемая дата
let selectedDate = null; // Выбранная дата

// Массивы для названий
const months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
];

const daysOfWeek = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"];

// Функция для отображения календаря на текущий месяц
function renderCalendar() {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    
    // Обновляем заголовок
    const monthYearDisplay = document.getElementById("current-month-year");
    if (monthYearDisplay) {
        monthYearDisplay.textContent = `${months[month]} ${year}`;
    }
    
    // Создаем таблицу календаря
    const calendarContainer = document.getElementById("calendar-container");
    if (!calendarContainer) return;
    
    calendarContainer.innerHTML = "";
    
    const table = document.createElement("table");
    table.className = "calendar-table";
    
    // Создаем заголовок с днями недели
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");
    
    daysOfWeek.forEach(day => {
        const th = document.createElement("th");
        th.textContent = day;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);
    
    // Создаем тело таблицы
    const tbody = document.createElement("tbody");
    
    // Получаем первый день месяца и количество дней
    const firstDay = new Date(year, month, 1);
    const startDayOfWeek = firstDay.getDay();
    // Корректируем, чтобы неделя начиналась с понедельника
    let startOffset = startDayOfWeek === 0 ? 6 : startDayOfWeek - 1;
    
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    
    let dayCounter = 1;
    let row = document.createElement("tr");
    
    // Заполняем пустые ячейки в начале месяца
    for (let i = 0; i < startOffset; i++) {
        const td = document.createElement("td");
        td.textContent = "";
        td.className = "empty-cell";
        row.appendChild(td);
    }
    
    // Заполняем дни месяца
    for (let day = 1; day <= daysInMonth; day++) {
        const td = document.createElement("td");
        td.textContent = day;
        
        // Проверяем, является ли день выходным
        const currentDay = new Date(year, month, day);
        const dayOfWeekNum = currentDay.getDay();
        if (dayOfWeekNum === 0 || dayOfWeekNum === 6) {
            td.classList.add("weekend");
        }
        
        // Проверяем, является ли день сегодняшним
        const today = new Date();
        if (today.getFullYear() === year && 
            today.getMonth() === month && 
            today.getDate() === day) {
            td.classList.add("today");
        }
        
        // Проверяем, является ли день выбранным
        if (selectedDate && 
            selectedDate.getFullYear() === year && 
            selectedDate.getMonth() === month && 
            selectedDate.getDate() === day) {
            td.classList.add("selected");
        }
        
        // Добавляем обработчик клика
        td.addEventListener("click", (function(y, m, d) {
            return function() {
                selectDate(y, m, d);
            };
        })(year, month, day));
        
        row.appendChild(td);
        
        // Если дошли до воскресенья или конец месяца, создаем новую строку
        if ((dayOfWeekNum === 0 && day !== daysInMonth) || day === daysInMonth) {
            // Заполняем пустые ячейки в конце строки
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

// Функция для обработки выбора даты
function selectDate(year, month, day) {
    selectedDate = new Date(year, month, day);
    
    const selectedDateDisplay = document.getElementById("selected-date");
    if (selectedDateDisplay) {
        selectedDateDisplay.textContent = `Выбранная дата: ${day} ${months[month]} ${year} года`;
        
        // Добавляем анимацию
        selectedDateDisplay.style.opacity = "0";
        setTimeout(() => {
            selectedDateDisplay.style.opacity = "1";
        }, 100);
    }
    
    // Перерисовываем календарь, чтобы подсветить выбранную дату
    renderCalendar();
}

// Функция для перехода на предыдущий месяц
function prevMonth() {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();
}

// Функция для перехода на следующий месяц
function nextMonth() {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();
}

// Функция для быстрого перехода к текущему месяцу
function goToToday() {
    currentDate = new Date();
    renderCalendar();
}

// Инициализация календаря
function initCalendar() {
    currentDate = new Date();
    selectedDate = null;
    renderCalendar();
}

// Добавляем кнопку "Сегодня" в HTML
// Эту функцию нужно вызвать после загрузки страницы
document.addEventListener("DOMContentLoaded", function() {
    initCalendar();
});

// =====================================
// ЗАДАЧА 3: DOM Дерево (Только формы)
// =====================================
// ========== ЗАДАЧА 3: ПОИСК СПИСКОВ В DOM ==========
document.addEventListener("DOMContentLoaded", function() {
    const countBtn = document.getElementById("count-btn");
    
    if (countBtn) {
        countBtn.addEventListener("click", function() {
            // Находим все списки (ul и ol) в документе
            const ulLists = document.getElementsByTagName("ul");
            const olLists = document.getElementsByTagName("ol");
            
            // Общее количество списков
            const totalLists = ulLists.length + olLists.length;
            
            // Собираем все списки в массив для детальной информации
            const allLists = [...ulLists, ...olLists];
            
            // Формируем результат
            const result = document.getElementById("dom-result");
            if (result) {
                result.innerHTML = `
                    <strong>Найдено списков: ${totalLists}</strong><br>
                    - Маркированных списков (&lt;ul&gt;): ${ulLists.length}<br>
                    - Нумерованных списков (&lt;ol&gt;): ${olLists.length}
                `;
                
                // Добавляем визуальное выделение найденных списков
                highlightLists(allLists);
            }
        });
    }
});

// Функция для подсветки найденных списков
function highlightLists(lists) {
    // Убираем предыдущую подсветку
    document.querySelectorAll('.highlight-list').forEach(list => {
        list.classList.remove('highlight-list');
    });
    
    // Добавляем подсветку для найденных списков
    lists.forEach(list => {
        list.classList.add('highlight-list');
        
        // Автоматически убираем подсветку через 2 секунды
        setTimeout(() => {
            list.classList.remove('highlight-list');
        }, 2000);
    });
}
