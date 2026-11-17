"""
Melatih ulang model Random Forest untuk studi kasus kelayakan beasiswa.
Jalankan dari folder utama: python train_model.py
"""
import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/dataset_beasiswa.csv")
X = pd.get_dummies(df[["IPK", "Penghasilan Ortu", "Prestasi", "Kehadiran"]], dtype=int)
y = df["Kelayakan"]
model = RandomForestClassifier(
    n_estimators=3, max_depth=3, max_features=2,
    bootstrap=True, random_state=42, criterion="gini"
)
model.fit(X, y)
classes = list(model.classes_)
features = list(X.columns)

def convert_tree(estimator):
    tree = estimator.tree_
    def build(node):
        if tree.feature[node] < 0:
            values = tree.value[node][0].tolist()
            return {"leaf": True, "prediction": classes[max(range(len(values)), key=lambda i: values[i])]}
        index = int(tree.feature[node])
        return {
            "leaf": False, "feature": features[index], "threshold": float(tree.threshold[node]),
            "left": build(int(tree.children_left[node])),
            "right": build(int(tree.children_right[node]))
        }
    return build(0)

result = {
    "case": "Prediksi Kelayakan Penerima Beasiswa",
    "classes": classes,
    "trees": [convert_tree(t) for t in model.estimators_]
}
with open("web/model.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print("Model berhasil dilatih dan web/model.json diperbarui.")
print("Akurasi pada data latih:", round(model.score(X, y) * 100, 2), "%")
