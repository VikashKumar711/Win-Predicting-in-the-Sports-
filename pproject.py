import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv('/content/game_pridiction.csv')
print(df);

# Clean data
cleaned_df = df.dropna().drop(columns=["game_url", "game_id"])

# Describe data
print("\n--- Data Description ---\n")
print(cleaned_df.describe(include='all'))


cleaned_df['total_score'] = cleaned_df['home_score'] + cleaned_df['away_score']
fig, axes = plt.subplots(3, 2, figsize=(16, 18))

# 1. Scatter Plot: home_score vs away_score
sns.scatterplot(data=cleaned_df, x='home_score', y='away_score', ax=axes[0, 0])
axes[0, 0].set_title("Scatter Plot: Home Score vs Away Score")

# 2. Bar Chart: Avg home_score per team 
avg_home_score = cleaned_df.groupby('home_team')['home_score'].mean().sort_values(ascending=False).head(10)
avg_home_score.plot(kind='bar', ax=axes[0, 1], color='skyblue')
axes[0, 1].set_title("Bar Chart: Avg Home Score (Top 10 Teams)")
axes[0, 1].set_ylabel("Average Score")

# 3. Pie Chart: Game distribution among top 5 home teams
team_counts = cleaned_df['home_team'].value_counts().head(5)
axes[1, 0].pie(team_counts, labels=team_counts.index, autopct='%1.1f%%', startangle=140)
axes[1, 0].set_title("Pie Chart: Home Games (Top 5 Teams)")

# 4. Box Plot: Distribution of scores by game state
sns.boxplot(data=cleaned_df, x='state_of_game', y='home_score', ax=axes[1, 1])
axes[1, 1].set_title("Box Plot: Home Score by Game State")

# 5. Histogram: Distribution of total scores
sns.histplot(cleaned_df['total_score'], bins=20, kde=True, ax=axes[2, 0], color='salmon')
axes[2, 0].set_title("Histogram: Total Game Scores")

# 6. Line Plot: Average scores over seasons
season_scores = cleaned_df.groupby('season')[['home_score', 'away_score']].mean()
season_scores.plot(ax=axes[2, 1])
axes[2, 1].set_title("Line Plot: Average Scores Over Seasons")
axes[2, 1].set_ylabel("Average Score")