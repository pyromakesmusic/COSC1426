import pandas as pd
COLORS = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪"]
colors_df = pd.Series(data=COLORS)
def get_colors(color_list=COLORS):
    return

def rainbow_loop(df=colors_df):
    for row in range(10):
        pass
    return

def main():
    three_colors = COLORS * 1
    """
    for color in COLORS:
        print(color, end="")
    """
    """
    for square in range(10):
        for row in range(square):
            for col in range(row):
                for color in COLORS:
                    print(color, end="")
            print()
    """
    colors_deep_copy = COLORS[:]
    colors_deep_copy[2] = "yellow"
    print(colors_deep_copy)

main()