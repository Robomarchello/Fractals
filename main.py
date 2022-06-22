from src.scripts.app import App
            
if __name__ == '__main__':
    app = App((512, 512), 'Fractals', 60)

    app.loop()