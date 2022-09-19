(function () {
    const btnDelete = document.querySelectorAll('.btnDelete');

    btnDelete.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Fuiste descalificado')) {
                e.preventDefault();
            }
        });
    });
})();