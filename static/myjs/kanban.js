$.getJSON('http://localhost:8080/kanban/saved', function(data) {
    items = data;
    createVars()
});
 
function saveBoard() {
    var saved_board = [];

    items = document.getElementsByClassName("kanban-item");
    for (let item of items) { 
        //console.log(item.parentElement.parentElement.getAttribute('data-id'));
        saved_board.push(item.parentElement.parentElement.getAttribute('data-id'));
        //console.log(item.parentElement.parentElement.innerText);
        saved_board.push(item.parentElement.parentElement.innerText);
        //console.log(item.innerText);
        saved_board.push(item.innerText);
    };
    $.ajax({
    type: "POST",
    url: '/kanban/save',
        data: JSON.stringify(saved_board),
        contentType: 'application/json; charset=utf-8'
    });
};

function createVars() {
    KanbanTest = new jKanban({
        element : '#myKanban',
        gutter  : '10px',
        widthBoard: '400px',
        boards  :  items
    });


    toDoButton = document.getElementById('addToDo');
    toDoButton.addEventListener('click',function(){
        var title  = document.getElementById("AddItem").value;
        KanbanTest.addElement(
            '_todo',
            {
                'title': title
            }
        );
    });

    addBoardDelete = document.getElementById('addDelete');
    addBoardDelete.addEventListener('click', function () {
        KanbanTest.addBoards(
            [{
                'id' : '_delete',
                'title'  : 'DELETE',
                'class' : 'error',
                'item'  : [
                    {
                        'title':'Items to delete:',
                    }
                ]
            }]
        )
    });

    removeBoard = document.getElementById('removeBoard');
    removeBoard.addEventListener('click',function(){
        KanbanTest.removeBoard('_delete');
    });
}
