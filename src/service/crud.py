
from sqlalchemy.orm import Session
from src.model import model
from src.schema import schema


def get_product_by_product_id(db: Session, product_id: str):

    return db.query(model.Products).filter(model.Products.product_id == product_id).first()


def get_product_by_id(db: Session, sl_id: int):

    return db.query(model.Products).filter(model.Products.id == sl_id).first()


def get_products(db: Session):

    return db.query(model.Products).all()


def add_product_details_to_db(db: Session, product: schema.ProductAdd):

    mv_details = model.Products(
        movie_id=product.product id,
        movie_name=product.product_name,
        director=product.product_description,
        geners=product.product ,
        membership_required=movie.membership_required,
        cast=movie.cast,
        streaming_platform=movie.streaming_platform
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Movies(**movie.dict())


def update_product_details(db: Session, sl_id: int, details: schema.UpdateMovie):

    db.query(model.Movies).filter(model.Movies.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Movies).filter(model.Movies.id == sl_id).first()


def delete_product_details_by_id(db: Session, sl_id: int):

    try:
        db.query(model.Movies).filter(model.Movies.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)