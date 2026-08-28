const InputPrompt = require("../../models/input-prompt")
const openai = require('../config/openai');

module.exports ={
    async sentText(req, res){
        const openaiAPI = openai.configuration();
        const inputModel = new InputPrompt(req.body)
        try {
            const response = await openaiAPI.chat.completions.create(
                openai.textCompletion(
                    inputModel
                )
            );
            return res.status(200).json({
                success: true,
                data: response.choices[0].message.content
            });
        } catch (error) {
            return res.status(400).json({
                success: false,
                error: error.error ? error.error : "existe um erro no servidor"
            });
        }
    }
}