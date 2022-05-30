$(function() {

    $('.tabs-list').on('click', '.tab', function(e) {
        // En este caso, evita que se abran los links cuando se clique en ellos
        e.preventDefault();
    
        $('.tab').removeClass('active');
        $('.tab-content').removeClass('show');
    
        $(this).addClass('active');
        // Recoge el valor del href que es igual al id del contenido, y le añade la clase "show"
        $($(this).attr('href')).addClass('show');
    
    });
    
});
