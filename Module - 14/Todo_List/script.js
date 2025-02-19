// Get references to DOM elements
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

// Load tasks from localStorage
function loadTasks() {
    taskList.innerHTML = "";
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.forEach(task => addTaskToDOM(task));
}

// Save tasks to localStorage
function saveTasks() {
    const tasks = Array.from(taskList.children).map(li => li.firstChild.textContent);
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Add new task
function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText === "") {
        alert("Task cannot be empty!");
        return;
    }
    addTaskToDOM(taskText);
    saveTasks();
    taskInput.value = "";
}

// Add task to DOM
function addTaskToDOM(taskText) {
    const li = document.createElement("li");
    li.textContent = taskText;
    
    const editBtn = document.createElement("button");
    editBtn.textContent = "✏️";
    editBtn.onclick = () => editTask(li);
    
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "🗑️";
    deleteBtn.onclick = () => {
        li.remove();
        saveTasks();
    };
    
    li.appendChild(editBtn);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
}

// Edit task
function editTask(taskElement) {
    const newTaskText = prompt("Edit task:", taskElement.firstChild.textContent);
    if (newTaskText !== null && newTaskText.trim() !== "") {
        taskElement.firstChild.textContent = newTaskText.trim();
        saveTasks();
    }
}

// Load existing tasks on page load
window.onload = loadTasks;
