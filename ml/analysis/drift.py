from backend.app.services.metrics import kl_drift

if __name__ == '__main__':
    print(kl_drift([0.4,0.6],[0.5,0.5]))
