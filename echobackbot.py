from telegram import Update
import docx
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler
import nest_asyncio
import os

# Apply nest_asyncio to fix event loop issues
nest_asyncio.apply()


if not os.path.exists("downloads"):
    os.makedirs("downloads")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Send a .txt/ or .docx file, and I'll respond! , ah and Hello World !")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(f"You said: {text}. That's real, bro, fr!")


def extract_text(file_path: str) -> str:
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format. Please upload a .txt or .docx file.")

def  modify_text(text: str)-> str:
    text = text.replace('*', '**')
    text = text.replace('#','###')
    
    lines = text.split('\n')
    formatted_lines = []
    for i, line in enumerate(lines):
        if i % 10 == 0:
            time_stamp = f"{i//10 + 1}:00"
            formatted_lines.append(time_stamp + ' ' + line)
        else:
            formatted_lines.append(line)
    modified_text = '\n'.join(formatted_lines)
    return modified_text        

# Handler for document messages
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    file = await update.message.document.get_file()
    file_name = update.message.document.file_name  # Get the file name
    file_path = f"downloads/{file_name}"  # Save the file in the downloads directory

    
    await file.download_to_drive(file_path)

    try:
        
        text = extract_text(file_path)
        modified_text = modify_text(text)
        output_file_name = f"formatted_{file_name}"
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(modified_text)
        await update.message.reply_document(open(output_file_name, 'rb'))   
    except ValueError as e:
        await update.message.reply_text(str(e))
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")
    finally:
        # Clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)

async def main() -> None:
    application = Application.builder().token("8036667158:AAH2qisQDdnPdhRlbAnteSRzkmG65UhGmxw").build()

    
    application.add_handler(CommandHandler("start", start))

    # Register the message handler for normal text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))  

    # Start the bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())