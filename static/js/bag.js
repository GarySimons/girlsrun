// Bag Page - Update quantity on click

$('.update-link').click(function (e) {
    var form = $(this).prev('.update-form');
    form.submit();
})


// Bag Page - Window scroll

$('.btt-link').click(function (e) {
    window.scrollTo(0, 0)
})


