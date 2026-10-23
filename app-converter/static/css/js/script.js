
function fecharModal() {
    const modal = document.getElementById("modalResultado");

    if (modal) {
        modal.style.display = "none";
        modal.remove();
    }
}

document.addEventListener("click", function (evento) {
    if (evento.target.closest("#modalResultado .fechar")) {
        fecharModal();
    }

    if (evento.target.closest("#modalResultado .botao-entendi")) {
        fecharModal();
    }

    const modal = document.getElementById("modalResultado");

    if (modal && evento.target === modal) {
        fecharModal();
    }
});

document.addEventListener("keydown", function (evento) {
    if (evento.key === "Escape") {
        fecharModal();
    }
});
