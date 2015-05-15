#!/usr/bin/env python
import os
from app import app, db
from app.models import User, Follow, Role, Permission, Post, Comment
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from config import config


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
"""
def make_shell_context():
    return dict(app=app, db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
"""

app.config.from_object(config['development'])

def dbinit():
    db.drop_all()
    db.create_all()

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
