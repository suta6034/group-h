from typing import Dict, Literal


def predict2(
    type: Literal["genre", "artist", "album"],
    key: str,
    algorithm: Literal["knn", "svm", "rf"],
) -> Dict[str, str]:
    return {"type": type, "key": key, "algorithm": algorithm}
