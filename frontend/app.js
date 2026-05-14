const API = "http://localhost:5000/api";

// ── load on start ────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", loadUsers);

// ── show message ─────────────────────────────────────────────────────────────
function showMessage(text, type = "success") {
  const el = document.getElementById("message");
  el.textContent = text;
  el.className = `message ${type}`;
  el.classList.remove("hidden");
  setTimeout(() => el.classList.add("hidden"), 3000);
}

// ── load all users ────────────────────────────────────────────────────────────
async function loadUsers() {
  try {
    const res = await fetch(`${API}/users`);
    const users = await res.json();
    const tbody = document.getElementById("user-table");
    document.getElementById("count").textContent = users.length;

    if (users.length === 0) {
      tbody.innerHTML = `<tr><td colspan="5" style="text-align:center;color:#999">No users yet</td></tr>`;
      return;
    }

    tbody.innerHTML = users.map(u => `
      <tr>
        <td>${u.id}</td>
        <td>${escape(u.name)}</td>
        <td>${escape(u.email)}</td>
        <td>${new Date(u.created_at).toLocaleDateString()}</td>
        <td class="actions">
          <button class="edit-btn"   onclick="editUser(${u.id},'${escape(u.name)}','${escape(u.email)}')">Edit</button>
          <button class="delete-btn" onclick="deleteUser(${u.id})">Delete</button>
        </td>
      </tr>`).join("");
  } catch {
    showMessage("Failed to load users", "error");
  }
}

// ── save (create or update) ───────────────────────────────────────────────────
async function saveUser() {
  const id    = document.getElementById("user-id").value;
  const name  = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();

  if (!name || !email) { showMessage("Name and email are required", "error"); return; }

  const method = id ? "PUT" : "POST";
  const url    = id ? `${API}/users/${id}` : `${API}/users`;

  try {
    const res = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email })
    });
    const data = await res.json();
    if (!res.ok) { showMessage(data.error || "Error", "error"); return; }
    showMessage(id ? "User updated!" : "User created!");
    resetForm();
    loadUsers();
  } catch {
    showMessage("Request failed", "error");
  }
}

// ── edit ──────────────────────────────────────────────────────────────────────
function editUser(id, name, email) {
  document.getElementById("user-id").value   = id;
  document.getElementById("name").value      = name;
  document.getElementById("email").value     = email;
  document.getElementById("form-title").textContent = "Edit User";
  document.getElementById("cancel-btn").classList.remove("hidden");
  document.getElementById("save-btn").textContent = "Update";
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ── delete ────────────────────────────────────────────────────────────────────
async function deleteUser(id) {
  if (!confirm("Delete this user?")) return;
  try {
    const res = await fetch(`${API}/users/${id}`, { method: "DELETE" });
    const data = await res.json();
    if (!res.ok) { showMessage(data.error || "Error", "error"); return; }
    showMessage("User deleted!");
    loadUsers();
  } catch {
    showMessage("Request failed", "error");
  }
}

// ── reset form ────────────────────────────────────────────────────────────────
function resetForm() {
  document.getElementById("user-id").value = "";
  document.getElementById("name").value    = "";
  document.getElementById("email").value   = "";
  document.getElementById("form-title").textContent = "Add User";
  document.getElementById("cancel-btn").classList.add("hidden");
  document.getElementById("save-btn").textContent = "Save";
}

// ── escape html ───────────────────────────────────────────────────────────────
function escape(str) {
  return String(str)
    .replace(/&/g,"&amp;").replace(/</g,"&lt;")
    .replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}