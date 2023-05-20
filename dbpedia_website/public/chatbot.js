const dfMessenger = document.querySelector('df-messenger');
dfMessenger.addEventListener('event-type', function (event) {
    console.log("Chatbot loaded and initialized");
    dfMessenger.renderCustomText('Custom text');
    dfMessenger.addEventListener('event-type', function (event) {
        console.log("df-list-element-clicked"+event.detail.element.title);
    });
});