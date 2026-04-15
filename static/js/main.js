document.getElementById("load-btn").addEventListener("click", async () => {
  const list = document.getElementById("message-list");
  list.innerHTML = "<li>Loading...</li>";

  try {
    const response = await fetch("/api/messages");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);

    const messages = await response.json();
    list.innerHTML = "";

    messages.forEach((msg) => {
      const li = document.createElement("li");
      li.innerHTML = `
        <div class="author">${msg.author}</div>
        <div class="text">${msg.text}</div>
      `;
      list.appendChild(li);
    });
  } catch (err) {
    list.innerHTML = `<li>Error loading messages: ${err.message}</li>`;
  }
});
