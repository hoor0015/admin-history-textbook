# 3주차 개념도 생성 (벤담 공리의 원리, 클라우제비츠 전쟁론)
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


# ---------------------------------------------------------------- 그림 3-1
# 공리의 원리 논증 구조
fig, ax = plt.subplots(figsize=(10, 6.6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
ax.axis("off")

box(ax, 3.1, 10.0, 5.8, 1.6, "두 주권자: 쾌락과 고통\n(인간이 실제로 무엇을 하게 될지를 지배)",
    fc="#fdf9f4", ec="#c77b2f")
box(ax, 2.4, 6.9, 7.2, 1.9,
    "공리의 원리\n행위를 승인할지 부인할지의 기준\n= 당사자의 행복을 늘리는 경향인가, 줄이는 경향인가",
    fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 1.2, 4.0, 4.2, 1.6, "개인의 행위", fc="white", ec="#2f6fb0")
box(ax, 6.6, 4.0, 4.2, 1.6, "정부의 모든 조치\n(법률과 정책)", fc="white", ec="#2f6fb0")
box(ax, 2.4, 0.8, 7.2, 1.9,
    "공동체의 행복 = 구성원 개인 이익의 총합\n정부의 목적: 최대 다수의 최대 행복",
    fc="#faf8fc", ec="#7a5fa8", weight="bold")

arrow(ax, 6.0, 9.9, 6.0, 9.0)
arrow(ax, 4.6, 6.8, 3.3, 5.8)
arrow(ax, 7.4, 6.8, 8.7, 5.8)
arrow(ax, 3.3, 3.9, 4.8, 2.9)
arrow(ax, 8.7, 3.9, 7.2, 2.9)

ax.text(6.35, 9.45, "이 사실 위에 규범을 세운다", ha="left", fontsize=9.5, color="#555")
ax.text(6.0, 3.35, "같은 하나의 기준으로 판단", ha="center", fontsize=9.5, color="#555")
fig.savefig(FIG / "fig03_utility_structure.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 3-2
# 공리주의 계보와 현대 행정
fig, ax = plt.subplots(figsize=(12, 4.4))
ax.set_xlim(0, 13.6)
ax.set_ylim(0, 6)
ax.axis("off")
steps = [
    ("벤담 (1748-1832)", "『도덕과 입법의 원리에\n관한 서론』(1789)\n공리의 원리, 행복 계산", "#f5f9fd", "#2f6fb0"),
    ("밀 (1806-1873)", "『자유론』(1859)\n공리주의의 정교화\n국가 개입의 한계", "#f4fbf6", "#2f8f4e"),
    ("20세기 정책과학", "후생경제학\n비용편익분석\n(편익·비용의 화폐 환산)", "#faf8fc", "#7a5fa8"),
    ("현대 행정", "증거기반 정책\n정책평가·성과관리\n예비타당성조사", "#fdf9f4", "#c77b2f"),
]
for i, (t1, t2, fc, ec) in enumerate(steps):
    x = 0.4 + i * 3.4
    box(ax, x, 3.3, 2.9, 1.5, t1, fc=fc, ec=ec, weight="bold")
    box(ax, x, 0.5, 2.9, 2.4, t2, fc="white", ec=ec, fontsize=10)
    if i < 3:
        arrow(ax, x + 3.0, 4.05, x + 3.3, 4.05)
fig.savefig(FIG / "fig03_bentham_legacy.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 3-3
# 목적-수단 위계: 전쟁과 정책
fig, ax = plt.subplots(figsize=(11, 6.6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
ax.axis("off")

ax.text(3.1, 11.4, "클라우제비츠: 전쟁", ha="center", fontsize=12.5, fontweight="bold")
ax.text(8.9, 11.4, "행정: 정책", ha="center", fontsize=12.5, fontweight="bold")

box(ax, 1.2, 8.9, 3.8, 1.7, "정치적 목적\n(정부가 정한다)", fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 1.2, 6.0, 3.8, 1.7, "전쟁\n(목적을 이루는 수단)", fc="#f5f9fd", ec="#2f6fb0")
box(ax, 1.2, 3.1, 3.8, 1.7, "전략·전술·군대\n(수단을 움직이는 수단)", fc="white", ec="#2f6fb0")

box(ax, 7.0, 8.9, 3.8, 1.7, "정책 목적\n(정치가 정한다)", fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 7.0, 6.0, 3.8, 1.7, "정책 수단\n(법령·예산·조직·정보)", fc="#f4fbf6", ec="#2f8f4e")
box(ax, 7.0, 3.1, 3.8, 1.7, "집행 현장\n(일선 기관과 공무원)", fc="white", ec="#2f8f4e")

for x in (3.1, 8.9):
    arrow(ax, x, 8.8, x, 7.9)
    arrow(ax, x, 5.9, x, 5.0)
ax.text(5.95, 7.3, "수단은 목적에\n종속된다", ha="center", fontsize=10.5, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.4"))

box(ax, 1.2, 0.5, 9.6, 1.6,
    "마찰: 불확실한 정보, 무수한 작은 장애물, 우연\n→ 구상(설계)과 실행(집행) 사이의 간극",
    fc="#fdf9f4", ec="#c77b2f", fontsize=10.5)
arrow(ax, 3.1, 3.0, 3.6, 2.2, color="#c77b2f")
arrow(ax, 8.9, 3.0, 8.4, 2.2, color="#c77b2f")
fig.savefig(FIG / "fig03_ends_means.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 3-4
# 전쟁의 삼위일체
fig, ax = plt.subplots(figsize=(10, 6.8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
ax.axis("off")

box(ax, 4.9, 5.3, 2.2, 1.4, "전쟁", fc="#f5f9fd", ec="#2f6fb0", fontsize=13, weight="bold")

box(ax, 3.7, 9.6, 4.6, 1.9, "격정: 증오와 적대감\n(맹목적 본능에 가깝다)\n주로 국민의 몫",
    fc="#fdf9f4", ec="#c77b2f")
box(ax, 0.4, 1.2, 4.6, 1.9, "우연과 개연성의 놀이\n(자유로운 정신 활동)\n주로 지휘관과 군대의 몫",
    fc="#f4fbf6", ec="#2f8f4e")
box(ax, 7.0, 1.2, 4.6, 1.9, "정치의 도구라는 종속성\n(순수한 이성에 속한다)\n주로 정부의 몫",
    fc="#faf8fc", ec="#7a5fa8")

ax.text(6.0, 4.35, "세 경향 사이에서 균형을 잡아야 한다\n(어느 하나를 빼놓는 이론은 현실과 모순된다)",
        ha="center", fontsize=10.5, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.5"))

arrow(ax, 6.0, 9.5, 6.0, 6.9)
arrow(ax, 3.4, 3.2, 5.0, 5.2)
arrow(ax, 8.6, 3.2, 7.0, 5.2)
fig.savefig(FIG / "fig03_trinity.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig03_*.png'))])
