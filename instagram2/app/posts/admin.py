from django.contrib import admin

# Register your models here.
from posts.models import Post, PostImage, PostComment, PostLike


class PostImageInline(admin.TabularInline):
    # model에 어떤 모델을 사용할지 지정
    model = PostImage
    # InlineModelAdmin.extra = controls the number of extra forms the formset will display.
    extra = 1


class PostCommentInline(admin.TabularInline):
    model = PostComment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #  fields는 admin site에서 정보를 입력할때 수정할 부분들을 표시하게 해준다.
    # author 와 content 를 지정하면 사용자가 author 와 content 의 내용을 직접 입력 하겠다는 뜻이다.
    list_display = ('author', 'content', 'created')
    list_display_links = ('author', 'content')
    inlines = [
        PostCommentInline,
        PostImageInline,
    ]


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content')


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass


"""
ModelAdmin: admin 인터페이스에서 models.py을 각 클래스를 의미한다.

@register: decorator for registering ModelAdmin class

modelAdmin에 사용할수 있는 필드 속성들:
- exclude
- field : add 하고 change 페이지에 있는 레이아웃 변경, 관계형 필드와 default 필드는 표시되지 않기 때문에 fields에 올 수 없다.
- list_display : 모든 항목들이 있는 페이지(add, change하기전 페이지)의 레이아웃을 변경한다.
- list_display_link : 모든 항목들이 있는 페이지(add, change하기전 페이지)의 레이아웃에서 지정된 링크를 클릭시 해당 데이터로 이동
"""
