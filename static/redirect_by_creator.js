const pageCreatorElement = document.getElementById("creator_page");

pageCreatorElement.addEventListener("click", () => {
  axios.get("http://localhost:5000/creator").then((res) => {
    window.location.href = res.data.url;
  });
});
