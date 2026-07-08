# 1주차(1차시·2차시) 개념도 생성
# 실행: cd $HOME/default-uv-env && PYTHONIOENCODING=utf-8 VIRTUAL_ENV= uv run python "<이 파일 경로>"
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


# ---------------------------------------------------------------- 그림 1-1
# 교재 전체 지도: 기원 - 탄생 - 고전 - 전환 (3부 구조)
fig, ax = plt.subplots(figsize=(12, 5.6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis("off")

stages = [
    ("기원\n(1-3주)", "고대 중국과 로마\n공자 · 키케로\n벤담 · 클라우제비츠", "#f5f9fd", "#2f6fb0"),
    ("탄생\n(4-5주)", "엽관제와 개혁운동\n윌슨 · 굿나우", "#f4fbf6", "#2f8f4e"),
    ("고전\n(6-8주)", "테일러 · 베버\n화이트 · 해링 · 귤릭", "#faf8fc", "#7a5fa8"),
    ("전환\n(9-13주)", "머튼 · 사이먼 · 왈도\n린드블롬 · 프레드릭슨\n쉬크 · 드로어", "#fdf9f4", "#c77b2f"),
]
for i, (t1, t2, fc, ec) in enumerate(stages):
    x = 0.5 + i * 3.4
    box(ax, x, 5.6, 2.9, 1.9, t1, fc=fc, ec=ec, fontsize=12, weight="bold")
    box(ax, x, 2.6, 2.9, 2.5, t2, fc="white", ec=ec, fontsize=10)
    if i < 3:
        arrow(ax, x + 3.0, 6.55, x + 3.3, 6.55)

# 하단: 교재 3부 대응
box(ax, 0.5, 0.6, 6.3, 1.2, "1부. 행정과 행정학의 역사 (교재 I장)",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=10)
box(ax, 7.3, 0.6, 2.9, 1.2, "2부. 고전적 행정이론\n(교재 II장)",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=10)
box(ax, 10.7, 0.6, 2.9, 1.2, "3부. 후기 고전이론과\n이론적 전환 (교재 III장)",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=10)
ax.set_title("텍스트로 보는 행정사: 한 학기의 지도 (13주, 26개 장)", fontsize=14, pad=14)
fig.savefig(FIG / "fig01_roadmap.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 1-2
# 고전 읽기의 세 단계: 시대 맥락 - 논지 - 현대적 함의
fig, ax = plt.subplots(figsize=(11, 4.8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.axis("off")

steps = [
    ("① 시대 맥락", "누가, 언제, 어떤 세상에서,\n무엇에 답하려고 썼는가", "#f5f9fd", "#2f6fb0"),
    ("② 논지", "무엇을 주장하고\n무엇에 반대하는가,\n근거는 무엇인가", "#f4fbf6", "#2f8f4e"),
    ("③ 현대적 함의", "오늘의 행정에서\n어떤 제도와 논쟁으로\n살아 있는가", "#faf8fc", "#7a5fa8"),
]
for i, (t1, t2, fc, ec) in enumerate(steps):
    x = 0.6 + i * 4.3
    box(ax, x, 4.6, 3.5, 1.6, t1, fc=fc, ec=ec, fontsize=12, weight="bold")
    box(ax, x, 1.8, 3.5, 2.2, t2, fc="white", ec=ec, fontsize=10)
    if i < 2:
        arrow(ax, x + 3.6, 5.4, x + 4.2, 5.4)
ax.text(6.5, 0.7, "세 단계는 한 방향이 아니다. 함의를 따지다가 다시 맥락으로 돌아가 읽는 왕복이 고전 읽기다.",
        ha="center", fontsize=10.5, color="#333")
ax.set_title("고전 읽기의 세 단계", fontsize=14, pad=12)
fig.savefig(FIG / "fig01_reading.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 1-3
# 고대 행정 연표: 중국과 로마
fig, ax = plt.subplots(figsize=(12, 5.6))
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 9)
ax.axis("off")

# 중국 레인
box(ax, 0.4, 6.6, 1.6, 1.4, "중국", fc="#f5f9fd", ec="#2f6fb0", fontsize=12, weight="bold")
china = [
    ("공자\n(기원전 551-479)", 2.4),
    ("진의 통일\n(기원전 221)", 5.4),
    ("유교의 국가\n이념화(기원전 2세기)", 8.4),
    ("사대부 관료제와\n과거제(19세기까지)", 11.4),
]
for t, x in china:
    box(ax, x, 6.6, 2.6, 1.4, t, fc="white", ec="#2f6fb0", fontsize=9.5)
for x in (5.1, 8.1, 11.1):
    arrow(ax, x, 7.3, x + 0.28, 7.3, color="#2f6fb0")

# 로마 레인
box(ax, 0.4, 3.6, 1.6, 1.4, "로마", fc="#fdf9f4", ec="#c77b2f", fontsize=12, weight="bold")
rome = [
    ("공화정과 키케로\n(기원전 106-43)", 2.4),
    ("『의무론』 저술\n(기원전 44)", 5.4),
    ("행정 제국:\n군단과 세금", 8.4),
    ("서로마 멸망\n(476)", 11.4),
]
for t, x in rome:
    box(ax, x, 3.6, 2.6, 1.4, t, fc="white", ec="#c77b2f", fontsize=9.5)
for x in (5.1, 8.1, 11.1):
    arrow(ax, x, 4.3, x + 0.28, 4.3, color="#c77b2f")

# 유럽으로 이어지는 유산
box(ax, 2.4, 0.8, 11.6, 1.5,
    "유산: 중국의 시험으로 뽑는 관료(실적주의의 원형), 로마의 법과 공직 윤리, 군사 조직에서 온 행정의 말들(라인, 제복, 공복)",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=10)
arrow(ax, 7.0, 3.5, 7.0, 2.5, color="#5b6ee1")
ax.set_title("고대 행정의 연표: 최초의 행정국가(중국)와 최초의 행정제국(로마)", fontsize=14, pad=14)
fig.savefig(FIG / "fig01_timeline.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 1-4
# 군대와 행정의 상호의존 순환
fig, ax = plt.subplots(figsize=(10, 6.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 4.1, 8.0, 3.8, 1.5, "세금 징수\n(조세 행정)", fc="#f5f9fd", ec="#2f6fb0", fontsize=11)
box(ax, 8.4, 5.0, 3.2, 1.5, "규칙적 급여와\n보급(도로·병참)", fc="#f4fbf6", ec="#2f8f4e", fontsize=10.5)
box(ax, 4.1, 1.6, 3.8, 1.5, "군기와 규율\n(무리가 군대가 된다)", fc="#faf8fc", ec="#7a5fa8", fontsize=10.5)
box(ax, 0.4, 5.0, 3.2, 1.5, "정복과 질서 유지\n(조세 기반 확대)", fc="#fdf9f4", ec="#c77b2f", fontsize=10.5)

arrow(ax, 7.2, 7.9, 9.4, 6.7)
arrow(ax, 9.4, 4.9, 7.2, 2.9)
arrow(ax, 4.7, 2.9, 2.6, 4.9)
arrow(ax, 2.6, 6.7, 4.7, 7.9)

ax.text(6.0, 5.6, "효과적인 행정과\n효과적인 군대는\n서로를 전제한다", ha="center", va="center",
        fontsize=12, fontweight="bold", color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.6"))
ax.set_title("로마가 보여 준 순환: 행정이 먼저인가, 군대가 먼저인가", fontsize=14, pad=12)
fig.savefig(FIG / "fig01_army_admin.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig01_*.png"))])
