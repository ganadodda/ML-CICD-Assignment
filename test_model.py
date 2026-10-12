from model import train_model, predict_sample


def test_model_trains_and_accuracy_is_valid():
    model, accuracy = train_model()
    assert model is not None
    assert 0.0 <= accuracy <= 1.0


def test_prediction_is_valid_iris_class():
    model, _ = train_model()
    prediction = predict_sample(model, [[5.1, 3.5, 1.4, 0.2]])
    assert prediction in [0, 1, 2]


def test_model_has_expected_number_of_classes():
    model, _ = train_model()
    assert len(model.classes_) == 3
