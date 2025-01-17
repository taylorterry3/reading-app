from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Example reading passages and questions
passages = [
    {
        "id": 1,
        "title": "The Lost Puppy",
        "content": (
            "Once there was a puppy named Max. One day, he wandered away from his yard and got lost. "
            "Max looked around and saw a big park. He sniffed everywhere but couldn’t find his way home. "
            "A kind girl named Emma found Max and saw his collar. She called the number on it, and Max's owner came to pick him up."
        ),
        "questions": [
            "Why did Max get lost?",
            "Where did Max go when he got lost?",
            "How did Emma help Max?",
        ],
    },
    {
        "id": 2,
        "title": "Lila's Lemonade Stand",
        "content": (
            "Lila wanted to buy a new book, so she set up a lemonade stand. "
            "She worked hard to make lemonade and decorated her stand. "
            "Lots of people bought lemonade because it was a hot day. By the end of the day, Lila had enough money for her book."
        ),
        "questions": [
            "Why did Lila set up a lemonade stand?",
            "How did Lila decorate her stand?",
            "Why did many people buy Lila's lemonade?",
        ],
    },
    {
        "id": 3,
        "title": "Tommy’s Treehouse",
        "content": (
            "Tommy loved climbing trees. One day, he decided to build a treehouse with his dad. "
            "They worked all weekend, hammering and painting. When it was done, Tommy invited his friends over. "
            "They played games and told stories in the treehouse."
        ),
        "questions": [
            "What did Tommy and his dad build?",
            "How long did it take to build the treehouse?",
            "What did Tommy and his friends do in the treehouse?",
        ],
    },
    {
        "id": 4,
        "title": "Maya’s Magic Paintbrush",
        "content": (
            "Maya loved to paint. One day, she found a magic paintbrush in the attic. "
            "When she painted with it, her pictures came to life! She painted a bird, and it flew out of the paper. "
            "Maya decided to use her paintbrush to help her friends by painting things they needed."
        ),
        "questions": [
            "What did Maya find in the attic?",
            "What happened when Maya used the magic paintbrush?",
            "How did Maya help her friends?",
        ],
    },
    {
        "id": 5,
        "title": "The Helpful Ants",
        "content": (
            "In a grassy meadow, a group of ants found a picnic left behind by people. "
            "They carried crumbs back to their hill to store for winter. On the way, one ant got stuck under a big leaf. "
            "The other ants worked together to lift the leaf and free their friend."
        ),
        "questions": [
            "What did the ants find in the meadow?",
            "Why were the ants carrying crumbs back to their hill?",
            "How did the ants help their friend?",
        ],
    },
    {
        "id": 6,
        "title": "Sam’s Science Experiment",
        "content": (
            "Sam wanted to see what would happen if he planted seeds in different types of soil. "
            "He used sand, clay, and regular soil. After a week, only the seeds in the regular soil grew. "
            "Sam learned that plants need the right kind of soil to grow."
        ),
        "questions": [
            "What was Sam’s experiment about?",
            "What types of soil did Sam use?",
            "Which soil worked best for the seeds?",
        ],
    },
    {
        "id": 7,
        "title": "Ella and the Snowman",
        "content": (
            "Ella loved winter. When it snowed, she built a big snowman with her brother. "
            "They gave him a carrot nose, a scarf, and a hat. They played with the snowman every day until the sun melted him away."
        ),
        "questions": [
            "What did Ella and her brother build in the snow?",
            "What did they use to decorate the snowman?",
            "What happened to the snowman when the sun came out?",
        ],
    },
    {
        "id": 8,
        "title": "Ben’s Big Catch",
        "content": (
            "Ben went fishing with his grandpa at the lake. He waited patiently, and finally, he caught a big fish. "
            "Ben was so excited that he took a picture with the fish before letting it go back into the water."
        ),
        "questions": [
            "Who did Ben go fishing with?",
            "What did Ben catch at the lake?",
            "What did Ben do with the fish after catching it?",
        ],
    },
    {
        "id": 9,
        "title": "The School Garden",
        "content": (
            "Mrs. Lee’s class started a garden behind the school. They planted flowers, vegetables, and herbs. "
            "Each student had a job, like watering the plants or pulling weeds. At the end of the year, they picked the vegetables and shared them with their families."
        ),
        "questions": [
            "What did Mrs. Lee’s class do behind the school?",
            "What kinds of plants did the class grow?",
            "What did the students do with the vegetables at the end of the year?",
        ],
    },
    {
        "id": 10,
        "title": "The Friendly Dolphin",
        "content": (
            "At the beach, Mia saw a dolphin swimming near the shore. "
            "The dolphin jumped out of the water and made everyone laugh. "
            "Mia learned that dolphins are very smart and like to play near people."
        ),
        "questions": [
            "Where did Mia see the dolphin?",
            "What did the dolphin do near the shore?",
            "What did Mia learn about dolphins?",
        ],
    },
]


# Homepage: display the reading passage
@app.route("/")
def home():
    passage = passages[0]  # Show the first passage by default
    return render_template("home.html", passage=passage)


# Questions page: display comprehension questions
@app.route("/questions/<int:passage_id>")
def questions(passage_id):
    passage = next((p for p in passages if p["id"] == passage_id), None)
    if not passage:
        return "Passage not found", 404
    return render_template("questions.html", passage=passage)


# Handle answer submission
@app.route("/submit", methods=["POST"])
def submit():
    answers = request.form.getlist("answers")
    passage_id = request.form.get("passage_id")
    passage = next((p for p in passages if str(p["id"]) == passage_id), None)
    if not passage:
        return "Passage not found", 404
    return render_template("review.html", passage=passage, answers=answers)


if __name__ == "__main__":
    app.run(debug=True)
