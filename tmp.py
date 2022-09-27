from pathlib import Path

train_p = Path(
    "./datasets/VOCdevkit/VOC2012/sp_ppe_voc_all_combinations/train"
)
valid_p = Path(
    "./datasets/VOCdevkit/VOC2012/sp_ppe_voc_all_combinations/valid"
)
test_p = Path("./datasets/VOCdevkit/VOC2012/sp_ppe_voc_all_combinations/test")

with open("train.txt", "w") as f:
    for p in train_p.glob("*.jpg"):
        f.write(f"{p.stem}\n")

with open("valid.txt", "w") as f:
    for p in valid_p.glob("*.jpg"):
        f.write(f"{p.stem}\n")

with open("test.txt", "w") as f:
    for p in test_p.glob("*.jpg"):
        f.write(f"{p.stem}\n")
