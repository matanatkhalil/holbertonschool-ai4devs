function sortScores(scores) {
    const sortedScores = scores.sort((a, b) => a - b);
    return sortedScores;
}

function printLeaderboard(players) {
    const scores = players.map((player) => player.score);
    const sortedScores = sortScores(scores);

    console.log("Leaderboard scores:");
    for (const score of sortedScores) {
        console.log(score);
    }
}

const players = [
    { name: "Nora", score: 9 },
    { name: "Samir", score: 80 },
    { name: "Amina", score: 100 },
    { name: "Rashad", score: 25 }
];

printLeaderboard(players);

if (typeof module !== "undefined") module.exports = { sortScores };
