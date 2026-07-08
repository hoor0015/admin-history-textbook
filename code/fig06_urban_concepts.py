# 6주차 1차시 개념도 생성 (그림 6-1 연표, 그림 6-2 애덤스의 진단 구조도)
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


# ---------------------------------------------------------------- 그림 6-1
# 진보주의 시대 도시개혁 연표 (1883-1914)
events = [
    (1883, "펜들턴법 제정\n(연방 실적주의)", "#2f6fb0"),
    (1889, "제인 애덤스\n헐 하우스 설립", "#8a6d3b"),
    (1901, "갤버스턴\n위원회형 시정부", "#2f8f4e"),
    (1904, "스테펀스 『도시의 수치』\n애덤스 「지방행정의 문제」", "#8a6d3b"),
    (1906, "싱클레어 『정글』\n뉴욕 도시개선국 출발", "#2f6fb0"),
    (1910, "브랜다이스 철도운임 청문회\n(과학적 관리 명명)", "#c77b2f"),
    (1911, "테일러 『과학적 관리의 원칙』\n시정연구소 공직훈련학교", "#c77b2f"),
    (1912, "테일러 하원 증언\n우드로 윌슨 당선", "#c77b2f"),
    (1914, "데이턴\n시지배인제 시행", "#2f8f4e"),
]

fig, ax = plt.subplots(figsize=(13, 5.2))
ax.set_xlim(-0.7, len(events) - 0.3)
ax.set_ylim(-3.6, 3.9)
ax.axis("off")
ax.axhline(0, color="#888", lw=2, zorder=1)
for i, (yr, label, c) in enumerate(events):
    up = i % 2 == 0
    ytxt = 1.05 if up else -1.05
    ax.plot([i], [0], marker="o", ms=8, color=c, zorder=3)
    ax.plot([i, i], [0, 0.7 if up else -0.7], color=c, lw=1.2, zorder=2)
    ax.text(i, 0.35 if up else -0.35, str(yr), ha="center",
            va="bottom" if up else "top", fontsize=10, color="#333",
            fontweight="bold")
    ax.text(i, ytxt, label, ha="center",
            va="bottom" if up else "top", fontsize=9.3, color="#222",
            bbox=dict(fc="white", ec=c, boxstyle="round,pad=0.35", lw=1.1))
legend_items = [("행정 개혁", "#2f6fb0"), ("사회 개혁과 폭로", "#8a6d3b"),
                ("도시정부 구조 개혁", "#2f8f4e"), ("과학적 관리", "#c77b2f")]
for j, (name, c) in enumerate(legend_items):
    ax.text(-0.4 + j * 2.4, 3.55, "■ " + name, fontsize=10.5, color=c,
            fontweight="bold", va="center")
fig.tight_layout()
fig.savefig(FIG / "fig06_reform_timeline.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 6-2
# 애덤스가 진단한 도시행정 실패의 구조
fig, ax = plt.subplots(figsize=(11, 7.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
ax.axis("off")

box(ax, 0.6, 9.9, 5.0, 1.8, "18세기의 설계\n이상주의적 헌장, 영국법 모방,\n시민에 대한 불신", fc="#f5f9fd", ec="#2f6fb0", fontsize=10.5)
box(ax, 6.4, 9.9, 5.0, 1.8, "19세기의 현실\n산업화·도시화·이민으로\n폭발적으로 커진 대도시", fc="#fdf9f4", ec="#c77b2f", fontsize=10.5)
box(ax, 3.5, 7.4, 5.0, 1.5, "제도와 현실의 괴리", fc="#fbf8f2", ec="#8a6d3b", fontsize=12, weight="bold")
arrow(ax, 3.1, 9.8, 4.9, 9.0)
arrow(ax, 8.9, 9.8, 7.1, 9.0)
box(ax, 3.5, 5.2, 5.0, 1.4, "규제·단속 위주의 행정\n(시민 일상과 동떨어진 정부)", fc="white", ec="#8a6d3b", fontsize=10.5)
arrow(ax, 6.0, 7.3, 6.0, 6.7)
box(ax, 0.4, 2.8, 3.4, 1.6, "무관심한 시민\n(정부는 나와\n상관없는 존재)", fc="white", ec="#555", fontsize=10)
box(ax, 4.3, 2.8, 3.4, 1.6, "직업 정치인\n(머신 정치와 보스의\n번성)", fc="white", ec="#555", fontsize=10)
box(ax, 8.2, 2.8, 3.4, 1.6, "경찰과 불법 산업의\n유착\n(집행 불가능한 규제)", fc="white", ec="#555", fontsize=10)
arrow(ax, 4.6, 5.1, 2.4, 4.5)
arrow(ax, 6.0, 5.1, 6.0, 4.5)
arrow(ax, 7.4, 5.1, 9.6, 4.5)
box(ax, 2.8, 0.3, 6.4, 1.5, "애덤스의 처방: 더 많은 민주주의\n결과의 혜택보다 과정에 참여할 권리", fc="#f4fbf6", ec="#2f8f4e", fontsize=11, weight="bold")
arrow(ax, 6.0, 2.7, 6.0, 1.9, color="#2f8f4e")
fig.tight_layout()
fig.savefig(FIG / "fig06_addams_diagnosis.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig06_*.png'))])
