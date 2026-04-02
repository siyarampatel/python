import gymnasium as gym

env = gym.make("CartPole-v1")

state, _ = env.reset()

for _ in range(10):
    action = env.action_space.sample()  # random action
    state, reward, done, truncated, info = env.step(action)
    
    print("State:", state, "Reward:", reward)
    
    if done:
        state, _ = env.reset()

env.close()