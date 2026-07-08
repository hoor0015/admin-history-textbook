# 13주차 개념도 생성 (1차시·2차시 공용)
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


# ---------------------------------------------------------------- 그림 13-1
# 행정사 전체 연표: 기원에서 전환까지, 시대별 가치의 전환
fig, ax = plt.subplots(figsize=(14.5, 7.0))
ax.set_xlim(0, 21)
ax.set_ylim(0, 10)
ax.axis("off")
ax.set_title("행정사 100년의 궤적: 여섯 개의 국면과 네 개의 가치", fontsize=15, pad=14)

eras = [
    ("고대의 통치 사상", "공자 『논어』\n(기원전 6-5세기)\n키케로 『의무론』\n(기원전 44)", "#fbf8f2", "#8a6d3b"),
    ("국가목적과 합리성", "벤담 『도덕과 입법의\n원리 서론』(1789)\n클라우제비츠\n『전쟁론』(1832)", "#fbf8f2", "#8a6d3b"),
    ("행정학의 탄생", "펜들턴법(1883)\n윌슨 「행정학 연구」\n(1887)\n굿나우(1900)", "#f5f9fd", "#2f6fb0"),
    ("고전적 행정이론", "애덤스(1905)\n테일러(1911)\n베버(1922)·화이트(1926)\n해링(1936)·귤릭(1937)", "#f5f9fd", "#2f6fb0"),
    ("재성찰의 시작", "머튼(1940)\n사이먼(1946)\n왈도(1948)", "#faf8fc", "#7a5fa8"),
    ("합리성과 형평", "린드블롬(1959)\n쉬크(1966)·드로어(1967)\n미노브룩 회의(1968)\n프레드릭슨(1971)", "#f4fbf6", "#2f8f4e"),
]
for i, (title, body, fc, ec) in enumerate(eras):
    x = 0.4 + i * 3.4
    box(ax, x, 6.6, 3.0, 1.1, title, fc=fc, ec=ec, fontsize=11.5, weight="bold")
    box(ax, x, 3.4, 3.0, 2.9, body, fc="white", ec=ec, fontsize=9.5)
    if i < 5:
        arrow(ax, x + 3.1, 7.15, x + 3.35, 7.15)

# 시대별 지배 가치 띠
values = [
    (0.4, 6.4, "도덕\n(통치자의 자격)", "#8a6d3b"),
    (7.2, 6.4, "능률\n(과학적 관리)", "#2f6fb0"),
    (14.0, 3.0, "합리성\n(의사결정)", "#7a5fa8"),
    (17.4, 3.0, "형평\n(누구를 위한 행정인가)", "#2f8f4e"),
]
ax.text(0.4, 2.6, "지배 가치의 전환", fontsize=11, fontweight="bold", color="#333")
for x, w, label, color in values:
    ax.add_patch(FancyBboxPatch((x, 0.9), w, 1.3, boxstyle="round,pad=0.06",
                                fc=color, ec=color, alpha=0.15, lw=1.2))
    ax.text(x + w / 2, 1.55, label, ha="center", va="center", fontsize=10.5,
            color=color, fontweight="bold")
for x in (6.9, 13.7, 17.1):
    arrow(ax, x - 0.05, 1.55, x + 0.45, 1.55, color="#555")

fig.tight_layout()
fig.savefig(FIG / "fig13_timeline.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 13-2
# 이론과 실천의 상호작용: 문제 -> (제도/이론) -> (이론/제도)의 순환
fig, ax = plt.subplots(figsize=(13, 7.6))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10.6)
ax.axis("off")
ax.set_title("이론과 실천의 상호작용: 문제가 이론을 낳고 이론이 제도를 만든다", fontsize=14, pad=12)

C_PROB = ("#fdf9f4", "#c77b2f")   # 현실의 문제
C_THEO = ("#f5f9fd", "#2f6fb0")   # 이론
C_INST = ("#f4fbf6", "#2f8f4e")   # 제도

# 범례
for i, (label, (fc, ec)) in enumerate([("현실의 문제·개혁운동", C_PROB),
                                       ("이론의 응답", C_THEO),
                                       ("제도의 변화", C_INST)]):
    box(ax, 0.8 + i * 4.2, 9.3, 3.4, 0.8, label, fc=fc, ec=ec, fontsize=11, weight="bold")

rows = [
    [("엽관제의 폐해와\n가필드 암살(1881)", C_PROB), ("펜들턴법(1883)\n실적제의 확산", C_INST),
     ("윌슨 「행정학 연구」(1887)\n굿나우의 이원론(1900)", C_THEO), "개혁이 이론을 낳다"],
    [("도시화·이민과\n도시정부의 부패", C_PROB), ("애덤스의 도시행정론(1905)\n테일러의 과학적 관리(1911)", C_THEO),
     ("시정연구소(1906)\n예산회계법(1921)", C_INST), "이론이 제도를 만들다"],
    [("대공황과\n뉴딜의 정부 팽창", C_PROB), ("해링의 공익론(1936)\n귤릭의 POSDCORB(1937)", C_THEO),
     ("브라운로 위원회(1937)\n대통령실 창설(1939)", C_INST), "이론이 정부를 재설계하다"],
    [("베트남전·인종갈등\n1960년대의 격동", C_PROB), ("미노브룩 회의(1968)\n신행정학과 사회적 형평", C_THEO),
     ("시민참여의 제도화\n분권·형평 지향 행정", C_INST), "가치가 행정을 다시 정의하다"],
]
for r, row in enumerate(rows):
    y = 6.9 - r * 2.05
    caption = row[3]
    for i, (text, (fc, ec)) in enumerate(row[:3]):
        box(ax, 0.4 + i * 4.4, y, 3.6, 1.55, text, fc=fc, ec=ec, fontsize=9.8)
        if i < 2:
            arrow(ax, 4.1 + i * 4.4, y + 0.78, 4.7 + i * 4.4, y + 0.78)
    ax.text(12.9, y + 1.72, caption, ha="right", fontsize=9.5, color="#555", style="italic")

ax.text(6.5, 0.25, "제도의 변화는 새로운 문제를 낳고, 그 문제가 다시 다음 이론을 부른다 (순환)",
        ha="center", fontsize=10.5, color="#555", style="italic")
fig.tight_layout()
fig.savefig(FIG / "fig13_interaction.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 13-3
# 고전 간 대화 지도: 대립과 계승
fig, ax = plt.subplots(figsize=(13, 9.2))
ax.set_xlim(0, 13)
ax.set_ylim(0, 13.6)
ax.axis("off")
ax.set_title("고전 간 대화 지도: 다섯 개의 논쟁과 두 개의 계승", fontsize=14, pad=12)

pairs = [
    ("윌슨·굿나우\n정치와 행정의 분리", "해링\n재량 속의 공익 해석", "대립"),
    ("귤릭\n조직의 원리(POSDCORB)", "사이먼\n원리는 격언에 불과하다", "대립"),
    ("테일러\n유일 최선의 방법과 능률", "왈도·프레드릭슨\n능률도 하나의 가치다", "대립"),
    ("베버\n이념형 관료제의 정밀성", "머튼\n훈련된 무능과 목표 대치", "수정"),
    ("쉬크·드로어\n기획과 분석의 예산·정책", "린드블롬\n점증주의와 상호조정", "대립"),
]
for r, (left, right, kind) in enumerate(pairs):
    y = 11.3 - r * 1.85
    box(ax, 0.5, y, 4.6, 1.4, left, fc="#f5f9fd", ec="#2f6fb0", fontsize=10.2)
    box(ax, 7.9, y, 4.6, 1.4, right, fc="#fdf9f4", ec="#c77b2f", fontsize=10.2)
    arrow(ax, 5.3, y + 0.7, 7.7, y + 0.7, color="#c0392b", style="<|-|>", ls="--")
    ax.text(6.5, y + 0.95, kind, ha="center", fontsize=9.5, color="#c0392b")

# 계승 두 줄 (아래)
heirs = [
    ("공자·키케로\n통치자의 덕과 공공의 것", "프레드릭슨\n사회적 형평과 공직의 책임", "계승: 오래된 질문의 부활"),
    ("벤담\n최대 다수의 최대 행복(계산)", "쉬크·드로어\n비용편익분석과 그 한계", "계승: 계산의 현대적 후예"),
]
for r, (left, right, kind) in enumerate(heirs):
    y = 2.05 if r == 0 else 0.2
    box(ax, 0.5, y, 4.6, 1.4, left, fc="#fbf8f2", ec="#8a6d3b", fontsize=10.2)
    box(ax, 7.9, y, 4.6, 1.4, right, fc="#fbf8f2", ec="#8a6d3b", fontsize=10.2)
    arrow(ax, 5.3, y + 0.7, 7.7, y + 0.7, color="#2f6fb0", lw=1.6)
    ax.text(6.5, y + 0.95, kind, ha="center", fontsize=9.5, color="#2f6fb0")

fig.tight_layout()
fig.savefig(FIG / "fig13_dialogue.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 13-4
# 고전에서 이후의 흐름으로: 신공공관리·거버넌스·공공가치
fig, ax = plt.subplots(figsize=(12.5, 5.8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.axis("off")
ax.set_title("고전의 세 물줄기와 이후의 흐름", fontsize=14, pad=12)

streams = [
    ("관리와 능률의 물줄기\n윌슨·테일러·귤릭·쉬크", "신공공관리(NPM)\n1980-90년대: 후드(1991),\n오스본·게블러(1992)", "#f5f9fd", "#2f6fb0"),
    ("조정과 참여의 물줄기\n애덤스·해링·린드블롬", "거버넌스론\n1990년대: 로즈(1996),\n정부에서 협치로", "#f4fbf6", "#2f8f4e"),
    ("공익과 가치의 물줄기\n키케로·왈도·프레드릭슨", "공공가치론\n1995년: 무어,\n공공가치의 창출", "#faf8fc", "#7a5fa8"),
]
for i, (src, dst, fc, ec) in enumerate(streams):
    y = 5.4 - i * 2.3
    box(ax, 0.5, y, 4.8, 1.8, src, fc=fc, ec=ec, fontsize=10.5)
    box(ax, 7.7, y, 4.8, 1.8, dst, fc="white", ec=ec, fontsize=10.5)
    arrow(ax, 5.5, y + 0.9, 7.5, y + 0.9, color=ec)

ax.text(6.5, 0.25, "이름은 바뀌어도 질문은 계속된다: 능률인가 가치인가, 정부 혼자인가 함께인가",
        ha="center", fontsize=10.5, color="#555", style="italic")
fig.tight_layout()
fig.savefig(FIG / "fig13_future.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob("fig13_*.png"))])
