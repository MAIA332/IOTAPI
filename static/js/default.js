function openMenu() {
    var x = document.getElementById("nav");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }

function copyToClipboard() {
    var textToCopy = document.getElementById("text-copy");

    // Seleciona o texto na caixa de texto
    textToCopy.select();
    textToCopy.setSelectionRange(0, 99999); // Para dispositivos móveis

    // Copia o texto para a área de transferência 
    navigator.clipboard.writeText(copyText.value);

    alert('Texto copiado: ' + textToCopy.value);
}