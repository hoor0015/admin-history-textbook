# 5주차 개념도 생성 (윌슨 II, 굿나우)
# 실행: cd ~/default-uv-env && PYTHONIOENCODING=utf-8 VIRTUAL_ENV= uv run python "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
import koreanize_matplotlib  # noqa: E402,F401

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(exist_ok=True)


def box(ax, x, y, w, h, text, fc="#f5f9fd", ec="#2f6fb0", fontsize=11, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight)


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, color=color, lw=lw, linestyle=ls))


# ---------------------------------------------------------------- 그림 5-1
# 윌슨의 정치-행정 구분과 여론의 자리
fig, ax = plt.subplots(figsize=(11, 5.6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.axis("off")

box(ax, 0.8, 6.2, 4.6, 2.2,
    "정치 (politics)\n크고 보편적인 일들\n일반적 설계(정책의 큰 그림)",
    fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 0.8, 0.8, 4.6, 2.2,
    "행정 (administration)\n개별적이고 소소한 일들\n특별한 수단의 선택과 집행",
    fc="#f5f9fd", ec="#2f6fb0", weight="bold")
arrow(ax, 3.1, 6.1, 3.1, 3.2)
ax.text(3.4, 4.6, "과업을 정해 준다\n(직무를 주무르지는 않는다)",
        fontsize=10, color="#555", ha="left")

box(ax, 7.6, 3.6, 3.6, 2.0, "여론\n권위 있는 비평가", fc="#faf8fc", ec="#7a5fa8",
    weight="bold")
arrow(ax, 8.4, 5.7, 5.6, 7.0, color="#2f8f4e")
ax.text(7.9, 6.9, "큰 방향의 상시 감독 (O)", fontsize=10, color="#2f8f4e",
        ha="center")
arrow(ax, 8.4, 3.5, 5.6, 2.2, color="#c0392b", ls="--")
ax.text(8.0, 2.2, "일상 세부에 직접 개입 (X)\n\"서툴고 성가신 참견\"",
        fontsize=10, color="#c0392b", ha="center")
fig.tight_layout()
fig.savefig(FIG / "fig05_wilson_dichotomy.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 5-2
# 유럽 행정 기술의 미국화 (칼 가는 법의 논리)
fig, ax = plt.subplots(figsize=(11, 5.2))
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.axis("off")

box(ax, 0.5, 5.0, 3.6, 2.2, "유럽의 행정 기술\n(프로이센·프랑스)\n군주정이 갈고닦은 방법",
    fc="#fdf9f4", ec="#c77b2f")
box(ax, 4.9, 5.0, 3.6, 2.2, "여과 장치\n우리의 헌법으로 거르고\n비판의 불로 증류한다",
    fc="#faf8fc", ec="#7a5fa8")
box(ax, 9.3, 5.0, 3.2, 2.2, "미국의 민주행정\n국민을 주권자로\n섬기는 기술",
    fc="#f5f9fd", ec="#2f6fb0")
arrow(ax, 4.2, 6.1, 4.8, 6.1)
arrow(ax, 8.6, 6.1, 9.2, 6.1)

box(ax, 1.6, 1.2, 4.4, 1.8, "빌리는 것\n일하는 방식 = 칼 가는 법",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=10.5)
box(ax, 7.0, 1.2, 4.4, 1.8, "빌리지 않는 것\n정치 원리 = 살인의 의도",
    fc="#fdf9f4", ec="#c0392b", fontsize=10.5)
arrow(ax, 3.8, 3.1, 5.5, 4.9, color="#2f8f4e")
arrow(ax, 9.2, 3.1, 7.6, 4.9, color="#c0392b", ls="--")
ax.text(6.5, 0.4, "정치와 행정의 구분이 있기에 이 선별이 안전해진다",
        ha="center", fontsize=11, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.4"))
fig.tight_layout()
fig.savefig(FIG / "fig05_americanization.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 5-3
# 굿나우: 국가 의지의 표출과 집행
fig, ax = plt.subplots(figsize=(11, 6.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 4.0, 8.2, 4.0, 1.4, "국가 의지 (state will)", fc="white", ec="#555",
    weight="bold")
box(ax, 0.8, 5.2, 4.4, 2.0, "정치 (politics)\n국가 의지의 표출\n(정책의 결정)",
    fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 6.8, 5.2, 4.4, 2.0, "행정 (administration)\n국가 의지의 집행\n(정책의 실행)",
    fc="#f5f9fd", ec="#2f6fb0", weight="bold")
arrow(ax, 4.6, 8.1, 3.0, 7.4)
arrow(ax, 7.4, 8.1, 9.0, 7.4)
arrow(ax, 5.3, 6.2, 6.7, 6.2)
ax.text(6.0, 6.5, "통제(조화)", fontsize=10, color="#555", ha="center")

labels = [
    ("사법 당국\n구체적 사건에\n법을 적용", 5.0),
    ("집행 당국\n집행의 전반적\n감독", 7.5),
    ("행정 당국\n과학적·기술적·\n상업적 활동", 10.0),
]
for text, cx in labels:
    box(ax, cx - 1.1, 1.6, 2.2, 2.2, text, fc="#f4fbf6", ec="#2f8f4e", fontsize=9.5)
    arrow(ax, 9.0, 5.1, cx, 4.0, color="#2f8f4e")
ax.text(7.5, 0.9, "세 당국 모두 국가 의지의 '집행'에 종사한다", fontsize=10,
        color="#2f8f4e", ha="center")
box(ax, 0.4, 2.0, 3.2, 1.8, "미국의 해법\n정당 체제가 두 기능의\n조화를 매개한다",
    fc="#faf8fc", ec="#7a5fa8", fontsize=10)
arrow(ax, 2.0, 3.9, 2.6, 5.1, color="#7a5fa8", ls="--")
fig.tight_layout()
fig.savefig(FIG / "fig05_goodnow_functions.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 5-4
# 윌슨과 굿나우 비교
fig, ax = plt.subplots(figsize=(11, 6.4))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 0.8, 8.3, 4.8, 1.3, "우드로 윌슨, 「행정학 연구」(1887)",
    fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 6.4, 8.3, 4.8, 1.3, "프랭크 굿나우, 『정치와 행정』(1900)",
    fc="#f5f9fd", ec="#2f6fb0", weight="bold")

wilson = [
    "한 편의 학술지 논문\n(문제 제기, 연구의 선언)",
    "행정은 정치의 고유 영역 밖\n행정의 영역은 사업의 영역",
    "구분의 쓸모: 유럽 행정 기술을\n안전하게 배우기 위한 보호막",
]
goodnow = [
    "한 권의 책\n(체계적 이론화, 정교화)",
    "정치는 국가 의지의 표출\n행정은 그 의지의 집행",
    "구분의 귀결: 두 기능의 조화,\n정치의 행정 통제(정당의 매개)",
]
for i, (wt, gt) in enumerate(zip(wilson, goodnow)):
    y = 6.2 - i * 1.9
    box(ax, 0.8, y, 4.8, 1.6, wt, fc="white", ec="#c77b2f", fontsize=10)
    box(ax, 6.4, y, 4.8, 1.6, gt, fc="white", ec="#2f6fb0", fontsize=10)

box(ax, 2.6, 0.4, 6.8, 1.4,
    "정치-행정 이원론: 행정학이 정치학에서 독립할 이론적 근거",
    fc="#faf8fc", ec="#7a5fa8", fontsize=11, weight="bold")
arrow(ax, 3.2, 2.3, 4.6, 1.9, color="#7a5fa8")
arrow(ax, 8.8, 2.3, 7.4, 1.9, color="#7a5fa8")
fig.tight_layout()
fig.savefig(FIG / "fig05_wilson_goodnow.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig05_*.png'))])
