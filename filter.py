from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse
from slackclient import SlackClient
import time

engine = create_engine('sqlite:///listings.db', echo=False)

Base = declarative_base()

class Listing(Base):
    """
    A table to store data on craigslist listings.
    """

    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String, unique=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def do_filter(self, results):
    filteredresult = []
    for result in results:
        listing = session.query(Listing).filter_by(link=result["link"]).first()

        # Don't store the listing if it already exists.
        if listing is None:
            if result["htmlTitle"] is None or result["link"] is None:
                # If there is no string identifying which neighborhood the result is from, skip it.
                continue

            # Create the listing object.
            listing = Listing(
                title=result["htmlTitle"],
                link=result["link"]
            )

            # Save the listing so we don't grab it again.
            session.add(listing)
            session.commit()

            filteredresult.append(result)

    return filteredresult