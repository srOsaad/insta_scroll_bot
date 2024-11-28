import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: app
    visible: true
    width: 300
    height: 300
    title: "Insta Auto Scroll Bot"

    flags: Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint

    Column {
        anchors.centerIn: parent

        TextField {
            id: textField1
            width: 200
            placeholderText: "Swipe 5 -3 1 2"
            text: ""
        }

        TextField {
            id: textField2
            width: 200
            placeholderText: "duration per reel"
            text: ""
        }

        Switch {
            id: switchBtn
            text: "Reverse swipe"
            checked: false
        }

        Button {
            text: "Done"
            onClicked: {
                app.visible = false
                pyHandler.handleDone(textField1.text, textField2.text, switchBtn.checked);
            }
        }
    }
}
