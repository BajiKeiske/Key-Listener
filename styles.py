btn_default_style = """
    QPushButton {
        position: relative;
        border: none;
        background: transparent;
        padding: 0;
        outline: none;
        cursor: pointer;
        font-family: sans-serif;
    }

    QPushButton.shadow {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.25);
        border-radius: 8px;
        transform: translateY(2px);
        transition: transform 600ms cubic-bezier(0.3, 0.7, 0.4, 1);
    }

    QPushButton.edge {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 8px;
        background: linear-gradient(
            to left,
            hsl(217, 33%, 16%) 0%,
            hsl(217, 33%, 32%) 8%,
            hsl(217, 33%, 32%) 92%,
            hsl(217, 33%, 16%) 100%
        );
    }

    QPushButton.front {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 12px 28px;
        font-size: 1.25rem;
        color: white;
        background: hsl(217, 33%, 17%);
        border-radius: 8px;
        transform: translateY(-4px);
        transition: transform 600ms cubic-bezier(0.3, 0.7, 0.4, 1);
    }

    QPushButton:hover.shadow {
        transform: translateY(4px);
        transition: transform 250ms cubic-bezier(0.3, 0.7, 0.4, 1.5);
    }

    QPushButton:hover.front {
        transform: translateY(-6px);
        transition: transform 250ms cubic-bezier(0.3, 0.7, 0.4, 1.5);
    }

    QPushButton:active.shadow {
        transform: translateY(1px);
        transition: transform 34ms;
    }

    QPushButton:active.front {
        transform: translateY(-2px);
        transition: transform 34ms;
    }

    .QPushButton.front span {
        user-select: none;
    }
"""

btn_pressed_style = """
    QPushButton {
        background-color: #CC99FF;
        color: white;
        border: 2px solid #45a049;
        border-radius: 5px;
        font-size: 16px;
        padding: 10px;
        min-width: 40px;
    }
"""

label_style = """
    QLabel {
        font-size: 24px;
        border: 2px solid #aaa;
        border-radius: 5px;
        padding: 10px;
        background-color: #404040;
        min-height: 40px;
    }
"""