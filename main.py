import platform
from rich.console import Console 
import trainer
from trainer import game
from trainer.errors import GameOver

console = Console()
console.print(f"[bold yellow]Math Trainer {trainer.VERSION} · {platform.python_version()}[/]")

try:
    score = game.play(rounds=5, max_mistakes=3)
except GameOver as e:
    console.print(f"[bold red]{e}[/]")
except KeyboardInterrupt:
    console.print(f"[bold blue]Το διέκοψε ο χρηστης[/]")
else:
    console.print(f"[bold green]Τέλος! Το σκορ είναι {score}[/]")
finally:
    console.print(f"[bold magenta]Αντίο[/]")












