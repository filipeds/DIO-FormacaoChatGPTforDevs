const OpenAI = require('openai')
require("dotenv").config()

module.exports = class openai{

	static configuration(){
		return new OpenAI({
			apiKey: process.env.OPEN_AI_KEY,
		})
	}

	static textCompletion ({prompt}) {
    return 	{
			model:"gpt-4o-mini",
			messages:[{ role: "user", content: `${prompt}` }],
			temperature:0,
			max_tokens: 3500,
			top_p:1,
			frequency_penalty: 0.5,
			presence_penalty: 0
		}
  }
}
