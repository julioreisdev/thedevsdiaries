const form = document.getElementById("post-form");

addEventListener("submit", (e) => {
  e.preventDefault();

  const email = document.getElementById("input-email").value;
  const title = document.getElementById("input-title").value;
  const message = document.getElementById("input-message").value;

  axios
    .post("http://localhost:5000/posts", { email, title, message })
    .then((res) => {
      window.location.reload()
    })
    .catch(console.error);
  console.log({ email, title, message });
});
