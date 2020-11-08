import logging

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

LOG_FORMATTER = "[ %(levelname)s ] : %(asctime)s : %(message)s"

logging.basicConfig(level=logging.INFO, format=LOG_FORMATTER)


def check_results(test_y: np.ndarray, pred_y: np.ndarray) -> None:
    """ scoreをloggerで出力する
    """
    _f_score = f1_score(test_y, pred_y, average="weighted")
    _accuracy_score = accuracy_score(test_y, pred_y)
    _recall_score = recall_score(test_y, pred_y, average="weighted")
    _precision_score = precision_score(test_y, pred_y, average="weighted")

    results = {
        "accuracy": _accuracy_score,
        "recall": _recall_score,
        "precision": _precision_score,
        "f_score": _f_score,
    }
    for key, value in results.items():
        logging.info("%s: %s", key, value)


def main() -> None:
    wine_data = load_wine()
    data = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
    train_x, test_x, train_y, test_y = train_test_split(
        data, wine_data.target, random_state=42, shuffle=True
    )

    print(" ===== svm.SVC trained by raw data ===== ")
    svc_params = {"random_state": 42}
    svc = SVC(**svc_params)
    svc.fit(train_x, train_y)
    pred_y_svc_for_tree = svc.predict(train_x)
    pred_y_svc = svc.predict(test_x)
    check_results(test_y, pred_y_svc)

    print("\n ===== tree.DecisionTreeClassifier trained by raw data ===== ")
    tree_params = {"max_depth": 3}
    clf = tree.DecisionTreeClassifier(**tree_params)
    clf.fit(train_x, train_y)
    pred_y_tree = clf.predict(test_x)
    check_results(test_y, pred_y_tree)

    print(
        "\n ===== tree.DecisionTreeClassifier trained by the label from svm.SVC ===== "
    )
    clf_svm = tree.DecisionTreeClassifier(**tree_params)
    clf_svm.fit(train_x, pred_y_svc_for_tree)
    pred_y_tree_svc = clf_svm.predict(test_x)
    check_results(pred_y_svc, pred_y_tree_svc)
    tree.plot_tree(clf_svm, feature_names=data.columns)
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()

