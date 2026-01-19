from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.coder import coder_agent
from agents.reviewer import reviewer_agent

def run_multi_agent_system():
    print("\n🤖 Pure Gemini Multi-Agent AI System")
    print("-" * 50)

    task = input("Enter your task: ")

    print("\n🧠 Planner thinking...")
    plan = planner_agent(task)
    print(plan)

    print("\n🔍 Researcher analyzing...")
    research = researcher_agent(plan)
    print(research)

    print("\n💻 Coder building solution...")
    solution = coder_agent(research)
    print(solution)

    print("\n🧪 Reviewer evaluating quality...")
    review = reviewer_agent(solution)

    print("\n📊 AGENT CONFIDENCE SCORES")
    print("-" * 30)
    print(f"Quality Score    : {review['quality']}/100")
    print(f"Confidence Score : {review['confidence']}/100")
    print(f"Readiness Score  : {review['readiness']}/100")

    print("\n📝 Detailed Review")
    print("-" * 30)
    print(review["full_review"])

    print("\n✅ FINAL OUTPUT READY")

if __name__ == "__main__":
    run_multi_agent_system()
