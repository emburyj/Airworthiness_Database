from routes import build_app


app = build_app()

# Listener
if __name__ == "__main__":
    # app.run(port=3000, debug=True) # For local debugging
    app.run(port=2468, debug=False) # For production