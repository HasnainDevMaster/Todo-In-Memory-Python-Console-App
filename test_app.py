"""
Test script to verify the functionality of the Todo Console App
without running the interactive loop.
"""
from src.services.todo_service import TodoService
from src.cli.command_handler import CommandHandler


def test_todo_app():
    print("Testing Todo Console App functionality...")

    # Initialize services
    todo_service = TodoService()
    command_handler = CommandHandler(todo_service)

    # Test 1: Add tasks
    print("\n1. Testing add command:")
    response1 = command_handler.handle_command('add "Buy groceries" "Milk, bread, eggs"')
    print(f"   Response: {response1}")

    response2 = command_handler.handle_command('add "Walk the dog"')
    print(f"   Response: {response2}")

    # Test 2: List tasks
    print("\n2. Testing list command:")
    response3 = command_handler.handle_command('list')
    print(f"   Response:\n   {response3}")

    # Test 3: Complete a task
    print("\n3. Testing complete command:")
    response4 = command_handler.handle_command('complete 1')
    print(f"   Response: {response4}")

    # Test 4: List tasks again to see completion status
    print("\n4. Testing list command after completion:")
    response5 = command_handler.handle_command('list')
    print(f"   Response:\n   {response5}")

    # Test 5: Update a task
    print("\n5. Testing update command:")
    response6 = command_handler.handle_command('update 2 "Walk the cat" "And feed the fish"')
    print(f"   Response: {response6}")

    # Test 6: List tasks again to see updated task
    print("\n6. Testing list command after update:")
    response7 = command_handler.handle_command('list')
    print(f"   Response:\n   {response7}")

    # Test 7: Delete a task
    print("\n7. Testing delete command:")
    response8 = command_handler.handle_command('delete 1')
    print(f"   Response: {response8}")

    # Test 8: List tasks again to see deletion
    print("\n8. Testing list command after deletion:")
    response9 = command_handler.handle_command('list')
    print(f"   Response:\n   {response9}")

    # Test 9: Test error handling
    print("\n9. Testing error handling:")
    response10 = command_handler.handle_command('complete 999')
    print(f"   Response: {response10}")

    response11 = command_handler.handle_command('invalid command')
    print(f"   Response: {response11}")

    print("\nAll tests completed successfully!")


if __name__ == "__main__":
    test_todo_app()