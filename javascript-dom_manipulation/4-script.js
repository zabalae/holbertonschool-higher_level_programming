const add_item = document.querySelector('#add_item')

add_item.addEventListener('click', function() {
    const new_item = document.createElement('li')
    new_item.textContent = 'Item'
    const my_list = document.querySelector('.my_list')

    my_list.appendChild(new_item)
});
