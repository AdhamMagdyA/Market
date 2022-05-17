
$('form.registration-form').on('submit', function(e) {

    var that = $(this),
    url = 'localhost:8080/market/signup',
    type = that.attr('method'),
    data = {};

    that.find('[name]').each(function(index, value) {
        var that = $(this),
        name = that.attr('name'),
        value = that.val();
        data[name] = value;
    });
    alert('working')
    axios({
        method: type,
        url: url,
        data: data
    })
    .then(function(response) {
        alert(response);
        return true;
    })
    .catch(function(error) {
        alert(error);
        return false;
    });
    alert('done')

    return false;
});