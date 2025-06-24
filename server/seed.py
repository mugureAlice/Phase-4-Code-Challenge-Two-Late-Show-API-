from server.app import app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

def seed():
    with app.app_context():
        
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        User.query.delete()
        db.session.commit()

        
        user1 = User(username="alice")
        user1.set_password("password123")
        user2 = User(username="bob")
        user2.set_password("password456")

        db.session.add_all([user1, user2])
        db.session.commit()

        
        guest1 = Guest(name="Tom Hanks", occupation="Actor")
        guest2 = Guest(name="Bill Gates", occupation="Entrepreneur")
        guest3 = Guest(name="Oprah Winfrey", occupation="TV Host")

        db.session.add_all([guest1, guest2, guest3])
        db.session.commit()

       
        episode1 = Episode(date=date(2024, 6, 1), number=101)
        episode2 = Episode(date=date(2024, 6, 8), number=102)

        db.session.add_all([episode1, episode2])
        db.session.commit()

        
        appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
        appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode1.id)
        appearance3 = Appearance(rating=3, guest_id=guest3.id, episode_id=episode2.id)

        db.session.add_all([appearance1, appearance2, appearance3])
        db.session.commit()

        print("Database seeded successfully.")

if __name__ == "__main__":
    seed()
