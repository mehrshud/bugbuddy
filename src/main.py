import logging
from flask import Flask
from tensorflow import keras
from bugbuddy.config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/healthcheck', methods=['GET'])
def healthcheck() -> str:
    """
    Returns the health status of the BugBuddy service.
    
    Returns:
        str: A success message indicating the service is healthy.
    """
    try:
        # Load a sample model to check TensorFlow functionality
        _ = keras.models.load_model('sample_model.h5')
        return 'BugBuddy service is healthy.', 200
    except Exception as e:
        logging.error(f'Healthcheck failed: {str(e)}')
        return 'BugBuddy service is unhealthy.', 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=app.config['DEBUG'])

