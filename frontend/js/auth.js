const API_BASE = "http://localhost:8000/api";

async function authFetch(url, options = {}) {
    let access = localStorage.getItem("access");

    options.headers = {
        ...(options.headers || {}),
        "Content-Type": "application/json",
        Authorization: "Bearer " + access
    };

    let response = await fetch(url, options);

    // 🔴 access token expired
    if (response.status === 401) {
        const refreshed = await refreshToken();
        if (!refreshed) {
            logout();
            throw new Error("Session expired");
        }

        // retry original request
        access = localStorage.getItem("access");
        options.headers.Authorization = "Bearer " + access;
        response = await fetch(url, options);
    }

    return response;
}

async function refreshToken() {
    const refresh = localStorage.getItem("refresh");
    if (!refresh) return false;

    const res = await fetch(`${API_BASE}/token/refresh/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh })
    });

    if (!res.ok) return false;

    const data = await res.json();
    localStorage.setItem("access", data.access);
    return true;
}

function logout() {
    localStorage.clear();
    window.location.href = "index.html";
}
