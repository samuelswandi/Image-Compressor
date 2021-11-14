const downloadButton = document.querySelector("#downloadButton")
const image = document.querySelector("#after");

downloadButton.addEventListener('click', () => {
    console.log("clicked");
    const p = image.getAttribute('src');
    saveAs(p, "compressedImage");
})