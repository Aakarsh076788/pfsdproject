from backend.app.services.metrics import expected_calibration_error

if __name__ == '__main__':
    print(expected_calibration_error([0.3,0.7,0.9],[0,1,1]))
